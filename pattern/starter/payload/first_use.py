#!/usr/bin/env python3
"""Guarded first use of a verified generated instance. Never an installer or migration."""
import argparse
import contextlib
import datetime
try:
    import fcntl
except ImportError:
    fcntl = None
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import uuid

sys.dont_write_bytecode = True
MAX_FILE = 1_000_000
MAX_TOTAL = 4_000_000
MAX_JSON = 128_000
JOURNAL = '.director/.first-use.json'
LOCK = '.director/.first-use.lock'
RECEIPT = '.director/receipts/RECEIPT_setup.json'
INSTANCE = '.director/INSTANCE.json'
HEX = re.compile(r'[0-9a-f]{64}\Z')
PROJECT_ID = re.compile(r'PROJ-[0-9a-f]{32}\Z')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unique(pairs):
    value = {}
    for key, item in pairs:
        need(key not in value, 'duplicate JSON key')
        value[key] = item
    return value


def safe(path):
    path = Path(os.path.abspath(path))
    if sys.platform == 'darwin':
        for alias in ('/tmp', '/var', '/etc'):
            if str(path).startswith(alias + '/') and os.path.realpath(alias) == '/private' + alias:
                path = Path('/private' + str(path))
                break
    for part in (path, *path.parents):
        need(not part.is_symlink(), 'symlink in selected path')
    return path


def selected(project, name):
    need(isinstance(name, str) and 0 < len(name.encode()) <= 512 and
         all(p not in ('', '.', '..') for p in name.split('/')) and
         not name.startswith('/') and not any(ord(c) < 32 for c in name), 'unsafe project-relative path')
    return safe(project / name)


def signature(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def read(path, total, limit=MAX_FILE):
    path = safe(path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode), 'selected path is not a regular file')
        need(before.st_size <= min(limit, MAX_TOTAL - total[0]), 'selected input exceeds read bound')
        data = bytearray()
        while True:
            chunk = os.read(fd, min(65_536, limit + 1 - len(data)))
            if not chunk:
                break
            data.extend(chunk)
            need(len(data) <= min(limit, MAX_TOTAL - total[0]), 'selected input exceeds read bound')
        need(signature(before) == signature(os.fstat(fd)) and len(data) == before.st_size,
             'selected file changed during read')
        total[0] += len(data)
        return bytes(data)
    finally:
        os.close(fd)


def json_read(path, total):
    data = read(path, total, MAX_JSON)
    value = json.loads(data, object_pairs_hook=unique,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON value')))
    need(isinstance(value, dict), 'selected JSON must be an object')
    return value, digest(data)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fsync_directory(path):
    fd = os.open(safe(path), os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def create_json(path, value):
    """Publish a complete durable file exclusively; never replace a neighboring writer."""
    path = safe(path)
    data = (json.dumps(value, indent=2, ensure_ascii=True) + '\n').encode()
    need(len(data) <= MAX_JSON, 'generated evidence exceeds JSON bound')
    fd, temporary = tempfile.mkstemp(prefix='.first-use-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.link(temporary, path, follow_symlinks=False)
        fsync_directory(path.parent)
    finally:
        os.unlink(temporary)


@contextlib.contextmanager
def locked(path):
    fd = os.open(safe(path), os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600)
    try:
        need(stat.S_ISREG(os.fstat(fd).st_mode), 'writer lock is not a regular file')
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('first-use or native writer is busy; preserve it and retry after it finishes') from None
        need(os.fstat(fd).st_ino == safe(path).stat().st_ino, 'writer lock was replaced; reopen')
        yield
    finally:
        os.close(fd)


def fault(point):
    """Independent disposable tests may replace this function to simulate interruption."""


def transport(project, provenance_name, instance_name, completed=False):
    total = [0]
    provenance, provenance_sha = json_read(selected(project, provenance_name), total)
    need(type(provenance.get('schema_version')) is int and provenance['schema_version'] == 1 and provenance.get('kind') == 'generic-template-transport-provenance' and
         provenance.get('not_configured_project_state') is True and provenance.get('not_setup_acceptance') is True,
         'recognized transport-only template provenance required')
    source = provenance.get('source')
    need(isinstance(source, dict) and source.get('url') == 'https://github.com/bladnman/director_pattern' and
         isinstance(source.get('sha'), str) and re.fullmatch('[0-9a-f]{40}', source['sha']) and
         isinstance(source.get('pattern_tree_sha'), str) and re.fullmatch('[0-9a-f]{40}', source['pattern_tree_sha']) and
         type(source.get('published')) is bool, 'exact source URL, pin, tree and publication evidence required')
    need('local_delta' not in source or type(source['local_delta']) is bool, 'source local_delta must be explicit boolean')
    descriptor = provenance.get('first_use')
    need(isinstance(descriptor, dict) and set(descriptor) ==
         {'schema', 'instance_path', 'receipt', 'backend', 'hook_source', 'guards', 'optional_guards'} and
         type(descriptor['schema']) is int and descriptor['schema'] == 1 and
         descriptor['instance_path'] == instance_name == INSTANCE and descriptor['receipt'] == RECEIPT,
         'unsupported first-use descriptor')
    need(provenance.get('generated_setup_receipt') == RECEIPT, 'transport receipt pointer differs')
    backend = descriptor['backend']
    need(isinstance(backend, dict), 'missing selected backend')
    if backend.get('kind') == 'director-request-bundles':
        need(backend == {'kind': 'director-request-bundles', 'helper': '.director/tools/requests.py',
                         'config': '.director/config.json'}, 'unsupported native bootstrap route')
    else:
        need(set(backend) == {'kind', 'path'} and backend['kind'] == 'project-contract', 'unsupported selected backend')
        selected(project, backend['path'])
    instance, instance_sha = json_read(selected(project, instance_name), total)
    need(set(instance) == {'schema', 'kind', 'generation_id', 'template_id', 'root_path', 'provenance_sha256'} and
         type(instance['schema']) is int and instance['schema'] == 1 and instance['kind'] == 'generated-template-instance',
         'actual generated-instance marker required; generic seeds cannot initialize')
    need(isinstance(instance['generation_id'], str) and str(uuid.UUID(instance['generation_id'])) == instance['generation_id'],
         'invalid generation UUID')
    need(isinstance(provenance.get('template'), str) and provenance['template'].strip() and
         isinstance(instance['template_id'], str) and instance['template_id'].strip() and
         len(provenance['template'].encode()) <= 256 and len(instance['template_id'].encode()) <= 256 and
         instance['provenance_sha256'] == provenance_sha and isinstance(instance['root_path'], str),
         'invalid template labels or differing transport digest')
    managed = provenance.get('managed_files')
    need(isinstance(managed, dict) and 0 < len(managed) <= 256, 'missing or oversized managed hash map')
    checker_hash = managed.get('.director/startup_check.py')
    need(isinstance(checker_hash, str) and HEX.fullmatch(checker_hash) and
         digest(read(selected(project, '.director/startup_check.py'), total)) == checker_hash,
         'selected helper/guard lacks reviewed transport baseline or managed template drift; reviewed integration required')
    checker = load_module(selected(project, '.director/startup_check.py'), 'first_use_startup_check')
    for name in {'AGENTS.md', descriptor['hook_source']}:
        selected(project, name)
    hook_text = read(selected(project, descriptor['hook_source']), total).decode('utf-8')
    route, _ = checker.startup_route(hook_text, '.director', descriptor['hook_source'])
    if route == 'block':
        checker.project_section(hook_text, descriptor['hook_source'])
    required = {'AGENTS.md', '.director/first_use.py', '.director/FIRST_USE.md', '.director/.gitignore',
                *('.director/' + name for name in (checker.BLOCK_ROUTE if route == 'block' else checker.START_ROUTE))}
    if backend['kind'] == 'director-request-bundles':
        required |= {backend['helper'], '.director/engine/tools/requests.py'}
    else:
        required.add(backend['path'])
    guards = []
    for key in ('guards', 'optional_guards'):
        items = descriptor[key]
        need(isinstance(items, list) and len(items) <= 20 and len(items) == len(set(items)), 'invalid selected guards')
        for name in items:
            path = selected(project, name)
            if key == 'guards' or path.exists():
                if not completed or name in managed:
                    required.add(name)
                guards.append(name)
    required.add(descriptor['hook_source'])
    need(required <= set(managed), 'selected helper/guard lacks reviewed transport baseline')
    for name, expected in managed.items():
        need(isinstance(expected, str) and HEX.fullmatch(expected), 'invalid managed hash')
        path = selected(project, name)
        if not completed or name in {'.director/startup_check.py', '.director/first_use.py'}:
            need(digest(read(path, total)) == expected, 'managed template drift; reviewed integration required')
    need(digest(read(Path(__file__), total)) == managed['.director/first_use.py'], 'executing helper differs from selected transport')
    privacy_snapshots = {}
    for name in ('.gitignore', '.director/.gitignore'):
        path = selected(project, name)
        if path.exists():
            privacy_snapshots[name] = digest(read(path, total))
    return provenance, provenance_sha, descriptor, instance, instance_sha, guards, checker, privacy_snapshots


def empty_canonical_seed(project, name, managed):
    """Only reviewed empty placeholders and their structural directories are empty state."""
    root = selected(project, name)
    if not root.exists():
        return
    need(root.is_dir(), 'canonical requests or walks must be directories')
    allowed_files = {path for path, expected in (managed or {}).items()
                     if path.startswith(name + '/') and Path(path).name == '.gitkeep' and expected == digest(b'')}
    allowed_directories = {name}
    for path in allowed_files:
        parts = path.split('/')[:-1]
        allowed_directories.update('/'.join(parts[:length]) for length in range(1, len(parts) + 1))
    pending, visited = [root], 0
    while pending:
        path = safe(pending.pop())
        visited += 1
        need(visited <= 256, 'canonical placeholder inventory exceeds first-use bound')
        relative = path.relative_to(project).as_posix()
        if path.is_dir():
            need(relative in allowed_directories, 'unreviewed canonical directory; preserve existing custom project')
            with os.scandir(path) as entries:
                for entry in entries:
                    need(len(pending) + visited < 256, 'canonical placeholder inventory exceeds first-use bound')
                    pending.append(Path(entry.path))
        else:
            need(relative in allowed_files and read(path, [0], limit=0) == b'',
                 'canonical requests or walks are populated or unreviewed; preserve existing custom project')


def pristine(project, backend, expected_id=None, managed=None):
    """No canonical recovery or mature state is adopted by generated first use."""
    for name in ('.producer', '.program/state.json', '.director/state.json', '.director/.request-txn'):
        need(not selected(project, name).exists(), 'existing or pending canonical state requires its owner recovery route')
    if backend['kind'] == 'project-contract':
        need(not selected(project, '.director/config.json').exists(), 'custom project must not acquire a bundled config')
        for name in ('requests', 'walks'):
            empty_canonical_seed(project, name, managed)
        # The reviewed generic seed may contain initial journal/config files, but
        # an already-started manual tracker is not a pristine generated instance.
        pending = [selected(project, p) for p in
                   ('journal', '.team/activity', '.team/improvements', '.team/config.json')]
        visited = 0
        while pending:
            path = safe(pending.pop())
            if not path.exists():
                continue
            visited += 1
            need(visited <= 256, 'custom runtime inventory exceeds first-use bound')
            if path.is_dir():
                with os.scandir(path) as entries:
                    for entry in entries:
                        need(len(pending) + visited < 256, 'custom runtime inventory exceeds first-use bound')
                        pending.append(Path(entry.path))
            else:
                name = path.relative_to(project).as_posix()
                need(managed is not None and name in managed and digest(read(path, [0])) == managed[name],
                     'existing custom runtime data lacks reviewed seed baseline; preserve owner recovery')
        return
    for name in ('.team', '.program', 'requests', '.director/sources', '.director/requests'):
        path = selected(project, name)
        if path.exists():
            need(path.is_dir() and not any(path.iterdir()), 'existing tracker/data preserved; no generated bootstrap')
    config = selected(project, backend['config'])
    if config.exists():
        need(expected_id is not None, 'existing config without owned intent/receipt; restore evidence, never reinitialize')
        value, _ = json_read(config, [0])
        need(value == {'schema_version': 1, 'record_mode': 'tracked', 'request_store': {
            'schema_version': 2, 'format': 'director-request-bundles', 'project_id': expected_id}},
            'config differs from this exact first-use intent; preserve for owner recovery')


def validate_intent(intent, instance, instance_sha, provenance_sha, backend):
    need(set(intent) == {'schema', 'kind', 'generation_id', 'instance_sha256', 'provenance_sha256', 'project_id', 'created_at'} and
         type(intent['schema']) is int and intent['schema'] == 1 and intent['kind'] == 'generated-first-use-intent' and
         intent['generation_id'] == instance['generation_id'] and intent['instance_sha256'] == instance_sha and
         intent['provenance_sha256'] == provenance_sha and isinstance(intent['created_at'], str) and intent['created_at'].strip() and
         (isinstance(intent['project_id'], str) and PROJECT_ID.fullmatch(intent['project_id'])
          if backend['kind'] == 'director-request-bundles' else intent['project_id'] is None),
         'owned first-use intent differs; preserve for owner recovery')


def block_baseline(project, descriptor, checker):
    """SHA-256 of the managed Director block on the block route; None on the earlier START.md route."""
    text = read(selected(project, descriptor['hook_source']), [0]).decode('utf-8')
    route, hook = checker.startup_route(text, '.director', descriptor['hook_source'])
    return hook['block_sha256'] if route == 'block' else None


def validate_receipt(receipt, provenance, provenance_sha, descriptor, instance):
    need('director_block_sha256' not in receipt or
         (isinstance(receipt['director_block_sha256'], str) and HEX.fullmatch(receipt['director_block_sha256'])),
         'existing receipt differs from this exact generated setup; preserve for owner review')
    need(set(receipt) - {'director_block_sha256'} == {'schema_version', 'kind', 'generation_id', 'template', 'provenance_sha256',
                         'project_id', 'source', 'managed_files', 'backend', 'privacy', 'technical_check',
                         'first_use_intent', 'created_at'} and
         type(receipt['schema_version']) is int and receipt['schema_version'] == 1 and
         receipt['kind'] == 'generated-instance-technical-setup' and
         receipt['generation_id'] == instance['generation_id'] and receipt['template'] == instance['template_id'] and
         receipt['provenance_sha256'] == provenance_sha and receipt['source'] == provenance['source'] and
         receipt['managed_files'] == provenance['managed_files'] and receipt['backend'] == descriptor['backend'] and
         receipt['first_use_intent'] == JOURNAL and isinstance(receipt['created_at'], str) and receipt['created_at'].strip(),
         'existing receipt differs from this exact generated setup; preserve for owner review')
    project_id = receipt['project_id']
    need(isinstance(project_id, str) and PROJECT_ID.fullmatch(project_id)
         if descriptor['backend']['kind'] == 'director-request-bundles' else project_id is None,
         'receipt project identity is invalid for selected backend')
    technical = receipt['technical_check']
    privacy = receipt['privacy']
    need(isinstance(technical, dict) and technical.get('managed_hashes') == 'verified' and
         technical.get('native_startup') == 'unrun' and technical.get('human_acceptance') == 'unrun' and
         isinstance(privacy, dict) and privacy.get('source_warning_delivery') ==
         'not performed; resolve before actual source capture', 'technical receipt claims unsupported acceptance or warning delivery')


def video_privacy(project):
    """Read-only verification; the caller performs the actual adapter's prerequisites."""
    destinations = ['.director/INSTANCE.json', '.director/.first-use.json', '.director/.first-use.lock',
                    '.director/receipts/RECEIPT_setup.json', '.director/PROJECT.local.md',
                    'requests/', 'walks/', 'journal/', '.team/activity/', '.team/improvements/', '.team/config.json']
    def git(*args, quiet=False):
        result = subprocess.run(['git', '-C', str(project), *args],
                                stdout=subprocess.DEVNULL if quiet else subprocess.PIPE,
                                stderr=subprocess.DEVNULL, timeout=10,
                                env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'})
        need(quiet or len(result.stdout) <= MAX_JSON, 'privacy query exceeds output bound')
        return result
    root = git('rev-parse', '--show-toplevel')
    if root.returncode:
        need(not (project / '.git').exists(), 'Git privacy root is unavailable')
        # No index exists; exact local patterns must precede private writes.
        director_ignore = read(project / '.director/.gitignore', [0]).decode('utf-8').splitlines()
        root_ignore = read(project / '.gitignore', [0]).decode('utf-8').splitlines()
        need(all(p in director_ignore or '/' + p in director_ignore for p in
                 ('INSTANCE.json', '.first-use.json', '.first-use.lock', 'receipts/', 'PROJECT.local.md')) and
             all('/' + p in root_ignore for p in destinations[5:]), 'retain required private ignore patterns before first use')
        return 'no Git repository; local exclusion patterns checked; index verification due before staging'
    need(Path(os.fsdecode(root.stdout).strip()).resolve() == project, 'generated project is inside another Git root; privacy review required')
    for name in destinations:
        tracked = git('ls-files', '--error-unmatch', '--', name, quiet=True)
        need(tracked.returncode == 1, 'private destination tracked or index unavailable; adapter reconciliation required')
        ignored = git('check-ignore', '--no-index', '--quiet', '--', name, quiet=True)
        need(ignored.returncode == 0, 'private destination is not effectively excluded; follow video adapter')
    return 'actual Git root, private exclusions and absence from index checked read-only'


def ensure(root, instance_name=INSTANCE, provenance_name='.director/PROVENANCE.json'):
    need(fcntl is not None, 'first use requires POSIX fcntl; unsupported runtime')
    root = safe(root)
    need(root.name == '.director' and root.is_dir(), 'explicit existing .director root required')
    project = root.parent
    facts = transport(project, provenance_name, instance_name, completed=selected(project, RECEIPT).exists())
    provenance, provenance_sha, descriptor, instance, instance_sha, guards, checker, privacy = facts
    receipt_path = selected(project, descriptor['receipt'])
    backend = descriptor['backend']
    checker_args = dict(root=root, receipt_name=descriptor['receipt'], guards=guards, hook_source=descriptor['hook_source'])
    checker_args['config_name' if backend['kind'] == 'director-request-bundles' else 'backend_contract'] = backend.get('config', backend.get('path'))
    if receipt_path.exists():
        receipt, _ = json_read(receipt_path, [0])
        validate_receipt(receipt, provenance, provenance_sha, descriptor, instance)
        if backend['kind'] == 'director-request-bundles':
            checker_args['expect_project_id'] = receipt['project_id']
        checker.check(**checker_args)
        return {'status': 'existing', 'changed': False, 'receipt': descriptor['receipt'],
                'project_id': receipt.get('project_id'), 'next': 'run the normal read-only startup check and evaluate current authority'}
    need(instance['root_path'] == str(project), 'uninitialized instance belongs to another generation root')
    journal_path = selected(project, JOURNAL)
    prior = json_read(journal_path, [0])[0] if journal_path.exists() else None
    if prior is not None:
        validate_intent(prior, instance, instance_sha, provenance_sha, backend)
    pristine(project, backend, prior.get('project_id') if prior else None, provenance['managed_files'])
    privacy_status = video_privacy(project) if backend['kind'] == 'project-contract' else 'local ignore bytes retained; effective privacy/source-delivery duties remain with owner'
    with locked(selected(project, LOCK)):
        # Another first chat may have completed while this caller was classifying.
        if receipt_path.exists():
            return ensure(root, instance_name, provenance_name)
        facts = transport(project, provenance_name, instance_name)
        need(facts[1] == provenance_sha and facts[4] == instance_sha and facts[7] == privacy,
             'generated instance or privacy inputs changed during first use')
        prior = json_read(journal_path, [0])[0] if journal_path.exists() else None
        with locked(root / '.requests.lock') if backend['kind'] == 'director-request-bundles' else contextlib.nullcontext():
            pristine(project, backend, prior.get('project_id') if prior else None, provenance['managed_files'])
            if prior is None:
                intent = {'schema': 1, 'kind': 'generated-first-use-intent', 'generation_id': instance['generation_id'],
                          'instance_sha256': instance_sha, 'provenance_sha256': provenance_sha,
                          'project_id': 'PROJ-' + uuid.uuid4().hex if backend['kind'] == 'director-request-bundles' else None,
                          'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
                create_json(journal_path, intent)
            else:
                intent = prior
                validate_intent(intent, instance, instance_sha, provenance_sha, backend)
        fault('intent')
        native = None
        backend_operation = 'selected project contract; no bundled initialization'
        if backend['kind'] == 'director-request-bundles':
            # Recheck after durable intent and immediately before any selected code runs.
            need(transport(project, provenance_name, instance_name)[1:5] == facts[1:5], 'transport changed before native initialization')
            pristine(project, backend, intent['project_id'], provenance['managed_files'])
            if not selected(project, backend['config']).exists():
                initialized = subprocess.run([sys.executable, '-B', str(selected(project, backend['helper'])),
                                              'init', '--project-id', intent['project_id']],
                                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15)
                need(initialized.returncode == 0, 'native init refused; preserve owned intent and inspect native recovery')
                backend_operation = 'selected native init CLI created the chosen identity'
            else:
                backend_operation = 'reused exact empty config from owned intent; no initialization'
            need(transport(project, provenance_name, instance_name)[1:5] == facts[1:5], 'transport changed before native validation')
            native = load_module(selected(project, backend['helper']), 'first_use_native_requests')
        fault('initialized')
        with locked(root / '.requests.lock') if backend['kind'] == 'director-request-bundles' else contextlib.nullcontext():
            pristine(project, backend, intent['project_id'], provenance['managed_files'])
            if native:
                need(native.Store(root).validate() == {'valid': 0}, 'native first-use store must remain empty')
            need(transport(project, provenance_name, instance_name)[1:5] == facts[1:5], 'transport changed before receipt')
            receipt = {'schema_version': 1, 'kind': 'generated-instance-technical-setup',
                       'generation_id': instance['generation_id'], 'template': instance['template_id'],
                       'provenance_sha256': provenance_sha, 'project_id': intent['project_id'], 'source': provenance['source'],
                       'managed_files': provenance['managed_files'], 'backend': backend,
                       'privacy': {'local_ignore_snapshots': privacy, 'check': privacy_status,
                                   'source_warning_delivery': 'not performed; resolve before actual source capture'},
                       'technical_check': {'managed_hashes': 'verified', 'backend': 'valid empty native store' if native else 'selected project contract; no bundled store created',
                                           'backend_operation': backend_operation, 'recovered_owned_intent': prior is not None,
                                           'native_startup': 'unrun', 'human_acceptance': 'unrun', 'role_authority': 'actor evaluation required',
                                           'payload_publication': 'unpublished candidate against declared base' if provenance['source'].get('local_delta') or not provenance['source']['published'] else 'caller-declared published transport; not authenticated'},
                       'first_use_intent': JOURNAL, 'created_at': intent['created_at']}
            baseline = block_baseline(project, descriptor, checker)
            if baseline:
                receipt['director_block_sha256'] = baseline
            receipt_path.parent.mkdir(exist_ok=True)
            safe(receipt_path.parent)
            create_json(receipt_path, receipt)
            fault('receipt')
            checker.check(**checker_args)
        return {'status': 'prepared', 'changed': True, 'receipt': descriptor['receipt'], 'project_id': intent['project_id'],
                'recovered_owned_intent': prior is not None,
                'next': 'run the normal read-only startup check and evaluate current authority; bootstrap alone grants no badge'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['ensure'])
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--instance', required=True)
    parser.add_argument('--provenance', required=True)
    args = parser.parse_args()
    try:
        result = ensure(args.root, args.instance, args.provenance)
        code = 0
    except (ValueError, OSError, TypeError, KeyError, UnicodeError, RecursionError, ImportError, subprocess.SubprocessError) as error:
        # Only known messages are useful; decoder excerpts or OS paths may contain private data.
        gap = str(error)[:240] if type(error) is ValueError else 'selected evidence/runtime inaccessible or malformed; preserve it for owner review'
        result = {'status': 'blocked', 'gap': gap, 'changed': 'inspect owned intent; never assume rollback', 'badge': 'not granted'}
        code = 1
    output = json.dumps(result, ensure_ascii=True, separators=(',', ':'))
    if len(output.encode()) > 4095:
        output = '{"status":"blocked","gap":"first-use result exceeds output bound","badge":"not granted"}'
        code = 1
    print(output)
    return code


if __name__ == '__main__':
    raise SystemExit(main())

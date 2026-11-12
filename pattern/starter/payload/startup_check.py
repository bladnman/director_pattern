#!/usr/bin/env python3
"""Bounded read-only local startup evidence. No tracker import, history, network or writes."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

MAX_JSON = 512_000
MAX_FILE = 1_000_000
MAX_TOTAL = 4_000_000
CARDS = ('staffing', 'requests', 'supervision', 'knowledge', 'update-check', 'privacy', 'badge')
BLOCK_ROUTE = ('WORKER.md', 'OPERATIONS.md', 'startup_check.py', 'START.md', 'DIRECTOR.md',
               *('cards/' + name + '.md' for name in CARDS))
START_ROUTE = ('START.md', 'DIRECTOR.md', 'OPERATIONS.md', 'startup_check.py')
STUB = '<!-- director-redirect-stub -->'
SECTION_CAP = 3000
NEXT = ('Reads from before the latest summary or resume are gone. Before your first project action, '
        'do the Recovery steps in the AGENTS.md Director block; before each action in its table, '
        'read the card it names.')
NEXT_FAILED = ('Answer without the badge and state this gap. Before acting on it read '
               '.director/cards/badge.md. The Recovery steps and table in the AGENTS.md Director block still apply.')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def absolute(path):
    path = Path(os.path.abspath(path))
    # macOS system aliases are not project-controlled symlinks.
    if sys.platform == 'darwin':
        for alias in ('/tmp', '/var', '/etc'):
            if str(path).startswith(alias + '/') and os.path.realpath(alias) == '/private' + alias:
                path = Path('/private' + str(path))
                break
    return path


def safe(base, value):
    raw = Path(value)
    need('..' not in raw.parts and len(str(raw)) <= 512, 'unsafe selected path')
    path = absolute(raw if raw.is_absolute() else base / raw)
    need(path.is_relative_to(base), 'selected path escapes the project')
    for parent in (path, *path.parents):
        need(not parent.is_symlink(), 'symlink in selected path')
        if parent == base:
            break
    return path


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def read(path, limit, total):
    need(path.is_file(), 'missing selected file: ' + path.name)
    size = path.stat().st_size
    need(size <= limit and total[0] + size <= MAX_TOTAL, 'selected evidence exceeds read bound')
    with path.open('rb') as stream:
        data = stream.read(limit + 1)
    need(len(data) == size and len(data) <= limit, 'selected file changed or exceeds read bound')
    total[0] += len(data)
    return data


def json_object(path, limit, total):
    value = json.loads(read(path, limit, total), object_pairs_hook=no_duplicates,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON value')))
    need(isinstance(value, dict), 'selected JSON must be an object')
    return value


def baseline(receipt, selected, required=True):
    matches = []
    for name in ('managed', 'managed_files', 'installed_files'):
        values = receipt.get(name)
        if values is None:
            continue
        need(isinstance(values, (dict, list)) and len(values) <= 512, 'unsupported or oversized baseline map')
        if isinstance(values, dict):
            if selected in values:
                value = values[selected]
                matches.append(value if isinstance(value, str) else value.get('sha256') if isinstance(value, dict) else None)
        else:
            for item in values:
                need(isinstance(item, dict), 'invalid baseline entry')
                if item.get('path') == selected:
                    matches.append(item.get('installed_sha256', item.get('sha256')))
    if not matches and not required:
        return None
    need(matches and all(isinstance(h, str) and re.fullmatch('[0-9a-f]{64}', h) for h in matches),
         'missing/invalid baseline for ' + selected)
    need(len(set(matches)) == 1, 'conflicting baselines for ' + selected)
    return matches[0]


def instruction_lines(text):
    """Exclude Markdown code examples from structural hook evidence, not from actor reads."""
    lines = []
    fence = None
    for line in text.splitlines():
        if fence:
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(fence[1]) + r',}[ \t]*', line):
                fence = None
            lines.append('')
            continue
        opening = re.match(r' {0,3}(`{3,}|~{3,})', line)
        if opening:
            fence = (opening[1][0], len(opening[1]))
            lines.append('')
        else:
            lines.append('' if line.startswith(('    ', '\t')) else line)
    return lines


def marked(text, source, labels, what):
    """Return the lines and the one ordered marker pair of a supported standalone block."""
    lines = instruction_lines(text)
    markers = []
    for number, line in enumerate(lines):
        comment = re.fullmatch(r' {0,3}<!--[ \t]*(.*?)[ \t]*-->[ \t]*', line)
        if comment and comment[1].startswith(tuple(prefix for pair in labels for prefix in
                                                   (pair[0].split(':')[0], '/' + pair[0].split(':')[0]))):
            markers.append((number, comment[1]))
    need(len(markers) == 2 and tuple(label for _, label in markers) in labels, what + ': ' + source)
    return lines, markers


def references(body, target):
    return bool(re.search(r'(?<![\w/.-])(?:\./)?' + re.escape(target) + r'(?![\w/.-])', body))


HOOKS = {('director-starter:2', '/director-starter:2'), ('director-pattern:start', 'director-pattern:end')}


def startup_hook(text, target, source='AGENTS.md'):
    """Recognize one supported marked route; prose authority remains an actor judgment."""
    lines, markers = marked(text, source, HOOKS, 'missing, ambiguous or unsupported marked startup hook')
    body = '\n'.join(lines[markers[0][0] + 1:markers[1][0]])
    need(references(body, target), 'marked startup hook does not reference selected route: ' + target)
    return {'path': source, 'marker': markers[0][1], 'target': target,
            'scope': 'marked route structure only'}


def startup_route(text, root, source='AGENTS.md'):
    """Select the route the marked block names: the standing block (WORKER.md) or the earlier START.md."""
    lines, markers = marked(text, source, HOOKS, 'missing, ambiguous or unsupported marked startup hook')
    body = '\n'.join(lines[markers[0][0] + 1:markers[1][0]])
    start, worker = root + '/START.md', root + '/WORKER.md'
    if references(body, start):
        return 'start', startup_hook(text, start, source)
    need(references(body, worker), 'marked startup hook does not reference selected route: ' + worker)
    hook = startup_hook(text, worker, source)
    raw = text.splitlines()
    block = '\n'.join(raw[markers[0][0]:markers[1][0] + 1]) + '\n'
    hook['block_sha256'] = hashlib.sha256(block.encode()).hexdigest()
    hook['block_bytes'] = len(block.encode())
    return 'block', hook


def project_section(text, source='AGENTS.md'):
    """The project-owned settings section must sit in the same file as the standing block."""
    lines, markers = marked(text, source, {('director-project', '/director-project')},
                            'project section missing or ambiguous (one director-project pair required)')
    raw = text.splitlines()
    size = len(('\n'.join(raw[markers[0][0]:markers[1][0] + 1]) + '\n').encode())
    body = lines[markers[0][0] + 1:markers[1][0]]
    need(any(re.match(r'\s*[-*] Check command: *`[^`]+`', line) for line in body),
         'project section has no check command: restore its "- Check command: `...`" line: ' + source)
    need(size <= SECTION_CAP, 'project section exceeds ' + str(SECTION_CAP) + ' bytes (' + str(size) +
         '): move the roster to .director/ROSTER.md and name it in the section: ' + source)
    return {'path': source, 'bytes': size, 'cap': SECTION_CAP, 'within_cap': True}


def update_discovery(root):
    """Local cache only: says whether the daily metadata check is due. Never blocks."""
    try:
        policy = root / 'update-policy.json'
        if policy.is_file() and not policy.is_symlink() and policy.stat().st_size <= 64_000:
            if json.loads(policy.read_bytes()).get('mode') == 'off':
                return 'off'
        cache = root / '.update-check.json'
        if not cache.exists():
            return 'due'
        if cache.is_symlink() or not cache.is_file() or cache.stat().st_size > 64_000:
            return 'unknown'
        last = json.loads(cache.read_bytes()).get('last_attempt')
        if last is None:
            return 'due'
        if type(last) not in (int, float):
            return 'unknown'
        return 'due' if time.time() - last >= 24 * 60 * 60 else 'not_due'
    except (OSError, ValueError, AttributeError):
        return 'unknown'


def generated_receipt(receipt, project, config_name, backend_contract):
    """Validate only the new generated format; existing receipt formats stay supported."""
    if not (receipt.get('kind') == 'generated-instance-technical-setup' or
            'first_use_intent' in receipt or ('generation_id' in receipt and 'provenance_sha256' in receipt)):
        return False
    need(set(receipt) == {'schema_version', 'kind', 'generation_id', 'template', 'provenance_sha256',
                         'project_id', 'source', 'managed_files', 'backend', 'privacy', 'technical_check',
                         'first_use_intent', 'created_at'} and
         type(receipt.get('schema_version')) is int and receipt['schema_version'] == 1 and
         receipt['kind'] == 'generated-instance-technical-setup' and
         isinstance(receipt['generation_id'], str) and
         re.fullmatch('[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}', receipt['generation_id']) and
         isinstance(receipt['template'], str) and receipt['template'].strip() and
         isinstance(receipt['provenance_sha256'], str) and re.fullmatch('[0-9a-f]{64}', receipt['provenance_sha256']) and
         receipt['first_use_intent'] == '.director/.first-use.json' and
         isinstance(receipt['created_at'], str) and receipt['created_at'].strip(), 'invalid generated setup receipt header')
    managed = receipt['managed_files']
    source = receipt['source']
    need(isinstance(source, dict) and isinstance(source.get('pattern_tree_sha'), str) and
         re.fullmatch('[0-9a-f]{40}', source['pattern_tree_sha']) and
         ('local_delta' not in source or type(source['local_delta']) is bool), 'invalid generated source tree or delta evidence')
    need(isinstance(managed, dict) and 0 < len(managed) <= 256 and
         all(isinstance(k, str) and isinstance(v, str) and re.fullmatch('[0-9a-f]{64}', v)
             for k, v in managed.items()), 'invalid generated setup baselines')
    declaration = receipt['backend']
    need(isinstance(declaration, dict), 'missing generated backend declaration')
    if declaration.get('kind') == 'director-request-bundles':
        need(declaration == {'kind': 'director-request-bundles', 'helper': '.director/tools/requests.py',
                             'config': '.director/config.json'} and not backend_contract and
             safe(project, config_name or '.director/config.json') == safe(project, declaration['config']),
             'generated backend differs from selected native route')
        need(isinstance(receipt['project_id'], str) and re.fullmatch('PROJ-[0-9a-f]{32}', receipt['project_id']),
             'missing/invalid generated project identity')
    else:
        need(set(declaration) == {'kind', 'path'} and declaration['kind'] == 'project-contract' and
             isinstance(declaration['path'], str) and not Path(declaration['path']).is_absolute() and
             backend_contract and safe(project, declaration['path']) == safe(project, backend_contract) and
             config_name is None and receipt['project_id'] is None, 'generated backend differs from selected custom contract')
    technical, privacy = receipt['technical_check'], receipt['privacy']
    need(isinstance(technical, dict) and technical.get('managed_hashes') == 'verified' and
         technical.get('native_startup') == 'unrun' and technical.get('human_acceptance') == 'unrun' and
         isinstance(privacy, dict) and privacy.get('source_warning_delivery') ==
         'not performed; resolve before actual source capture', 'generated receipt claims unsupported acceptance or warning delivery')
    return True


def check(root, receipt_name=None, config_name=None, backend_contract=None, guards=(), expect_project_id=None,
          hook_source='AGENTS.md'):
    root = absolute(root)
    for part in (root, *root.parents):
        need(not part.is_symlink(), 'symlink in installation root')
    need(root.is_dir(), 'missing installation directory')
    project = root.parent
    total = [0]
    receipt_path = safe(project, receipt_name or str(root / 'install.json'))
    need(receipt_path.is_relative_to(root), 'receipt must be inside the installation')
    receipt = json_object(receipt_path, MAX_JSON, total)
    need(not receipt.get('not_setup_acceptance') and not receipt.get('not_configured_project_state'),
         'template provenance is not a configured installation receipt')
    is_generated = generated_receipt(receipt, project, config_name, backend_contract)
    source = receipt.get('source')
    need(isinstance(source, dict) and isinstance(source.get('url'), str) and source['url'].rstrip('/') == 'https://github.com/bladnman/director_pattern',
         'missing/unsupported installation source URL')
    need(isinstance(source.get('sha'), str) and re.fullmatch('[0-9a-f]{40}', source['sha']),
         'missing/invalid installation source pin')
    need(type(source.get('published')) is bool, 'missing installation source publication status')
    need(not Path(hook_source).is_absolute(), 'hook source must be project-relative')
    hook_path = safe(project, hook_source)
    hook_relative = hook_path.relative_to(project).as_posix()
    hook_text = read(hook_path, MAX_FILE, total).decode('utf-8')
    route, hook = startup_route(hook_text, root.relative_to(project).as_posix(), hook_relative)
    section = project_section(hook_text, hook_relative) if route == 'block' else None
    managed = [str(root / name) for name in (BLOCK_ROUTE if route == 'block' else START_ROUTE)]
    managed_paths = {safe(project, value).relative_to(project).as_posix() for value in managed}
    paths = ['AGENTS.md', *managed, *guards, hook_source]
    if backend_contract:
        paths.append(backend_contract)
    selected = {}
    for value in paths:
        path = safe(project, value)
        selected.setdefault(path.relative_to(project).as_posix(), path)
    need(len(selected) <= 30, 'too many selected startup guards')
    checked = []
    snapshots = []
    for relative, path in selected.items():
        expected = baseline(receipt, relative, required=relative in managed_paths)
        data = read(path, MAX_FILE, total)
        digest = hashlib.sha256(data).hexdigest()
        if route == 'start' and path == root / 'START.md':
            need(STUB not in data.decode('utf-8', 'replace'),
                 'marked block still routes to ' + relative + ', which is now a redirect stub: unfinished update; '
                 'merge the current Director block (UPDATES.md, "Move to the AGENTS.md block")')
        if relative in managed_paths:
            need(digest == expected, 'startup baseline mismatch: ' + relative)
        else:
            text = data.decode('utf-8')
            snapshots.append({'path': relative, 'snapshot': 'not_recorded' if expected is None else
                              'unchanged' if digest == expected else 'changed'})
        if relative == hook_relative:
            need(data.decode('utf-8') == hook_text, 'selected hook source changed during the check')
        checked.append(relative)
    if backend_contract:
        backend = {'kind': 'project-declared contract', 'path': safe(project, backend_contract).relative_to(project).as_posix(),
                   'scope': 'current project contract read; actor must resolve its actual lean/custom route; no JSON store assumed'}
    else:
        config_path = safe(project, config_name or str(root / 'config.json'))
        config = json_object(config_path, 64_000, total)
        need(type(config.get('schema_version')) is int and config['schema_version'] == 1, 'unsupported configuration schema header')
        need(isinstance(config.get('record_mode'), str) and config['record_mode'] in {'tracked', 'lean'},
             'unknown configuration mode')
        need(not is_generated or config['record_mode'] == 'tracked', 'generated native backend must remain tracked')
        if config['record_mode'] == 'tracked':
            store = config.get('request_store')
            need(isinstance(store, dict) and type(store.get('schema_version')) is int and store['schema_version'] == 2, 'unsupported tracked-store schema header')
            need(store.get('format') in {'director-request-bundles', 'request-bundles'}, 'unknown tracked-store format; use the actual project backend contract')
            need(isinstance(store.get('project_id'), str) and re.fullmatch('PROJ-[0-9a-f]{32}', store['project_id']), 'missing/invalid configured project identity')
            if is_generated:
                need(store['format'] == 'director-request-bundles' and store['project_id'] == receipt['project_id'],
                     'generated receipt differs from actual native store identity or format')
            expected = expect_project_id or receipt.get('project_id')
            if expected is not None:
                need(store['project_id'] == expected, 'configured project identity differs from selected project')
        backend = {'kind': 'configuration header', 'path': config_path.relative_to(project).as_posix(),
                   'schema_version': config['schema_version'], 'record_mode': config['record_mode']}
    result = {'status': 'evidence_matched', 'scope': 'managed evidence and marked route structure checked; current project instruction evaluation still required',
            'source_sha': source['sha'], 'source_published': source['published'],
            'source_local_delta': source.get('local_delta', 'not recorded'),
            'receipt': receipt_path.relative_to(project).as_posix(), 'checked_paths': checked,
            'startup_hook': hook, 'project_instruction_snapshots': snapshots,
            'actor_must_confirm': ['resolved Project Director role', 'all actual selected role/shared guards included in this command', 'authoritative canonical backend and config/contract binding',
                                  'effective host-loaded route and complete current project instructions, including conflicts outside the hook'],
            'backend': backend, 'bytes_read': total[0],
            'not_proved': ['instruction consumption or role authority', 'ledger/history integrity',
                           'native host behavior or effective model', 'human acceptance or live execution',
                           'semantic compatibility of project instructions'],
            'update_check': update_discovery(root), 'next': NEXT}
    if route == 'block':
        recorded = receipt.get('director_block_sha256')
        need(recorded is None or (isinstance(recorded, str) and re.fullmatch('[0-9a-f]{64}', recorded)),
             'invalid recorded Director block baseline')
        actual = hook.pop('block_sha256')
        need(recorded is None or recorded == actual,
             'Director block differs from its recorded baseline: the block is managed text; restore it from the '
             'installed revision (project wording belongs in the project section) or finish a reviewed update')
        result['director_block'] = 'not_recorded' if recorded is None else 'unchanged'
        if recorded is None:
            result['actor_must_confirm'].append('Director block has no recorded baseline: compare it with the installed revision')
        result['project_section'] = section
    else:
        result['route_note'] = 'earlier START.md route; the standing AGENTS.md block is the current route (UPDATES.md)'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).absolute().parent)
    parser.add_argument('--receipt', help='Exact project-root-relative installation receipt; no newest-file selection')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--config', help='Actual project-root-relative JSON config header, including external canonical trackers')
    group.add_argument('--backend-contract', help='Explicit already-read project-owned lean/custom backend contract; no store initialization')
    parser.add_argument('--guard', action='append', default=[], help='Additional already-read project-owned startup guard; current authority requires actor evaluation')
    parser.add_argument('--hook-source', default='AGENTS.md', help='Explicit project-relative file containing the supported marked hook; outer AGENTS is always read, actual host import requires actor evaluation')
    parser.add_argument('--expect-project-id', help='Stable actual project identity from the already-read project authority, when known')
    args = parser.parse_args()
    try:
        result = check(args.root, args.receipt, args.config, args.backend_contract, args.guard, args.expect_project_id,
                       args.hook_source)
        code = 0
    except (ValueError, OSError, TypeError, KeyError, UnicodeError, RecursionError) as error:
        result = {'status': 'blocked', 'scope': 'bounded local operational evidence only', 'gap': str(error)[:600],
                  'next': NEXT_FAILED}
        code = 1
    output = json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    if len(output.encode()) > 4096:
        output = json.dumps({'status':'blocked','gap':'startup result exceeds output bound'}, separators=(',', ':'))
        code = 1
    print(output)
    return code


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Bounded read-only local startup evidence. No tracker import, history, network or writes."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys

MAX_JSON = 512_000
MAX_FILE = 1_000_000
MAX_TOTAL = 4_000_000


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


def startup_hook(text, target, source='AGENTS.md'):
    """Recognize one supported marked route; prose authority remains an actor judgment."""
    lines = instruction_lines(text)
    markers = []
    for number, line in enumerate(lines):
        comment = re.fullmatch(r' {0,3}<!--[ \t]*(.*?)[ \t]*-->[ \t]*', line)
        if comment and comment[1].startswith(('director-starter', '/director-starter', 'director-pattern', '/director-pattern')):
            markers.append((number, comment[1]))
    supported = {('director-starter:2', '/director-starter:2'),
                 ('director-pattern:start', 'director-pattern:end')}
    need(len(markers) == 2 and tuple(label for _, label in markers) in supported,
         'missing, ambiguous or unsupported marked startup hook: ' + source)
    body = '\n'.join(lines[markers[0][0] + 1:markers[1][0]])
    need(re.search(r'(?<![\w/.-])(?:\./)?' + re.escape(target) + r'(?![\w/.-])', body),
         'marked startup hook does not reference selected route: ' + target)
    return {'path': source, 'marker': markers[0][1], 'target': target,
            'scope': 'marked route structure only'}


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
    source = receipt.get('source')
    need(isinstance(source, dict) and isinstance(source.get('url'), str) and source['url'].rstrip('/') == 'https://github.com/bladnman/director_pattern',
         'missing/unsupported installation source URL')
    need(isinstance(source.get('sha'), str) and re.fullmatch('[0-9a-f]{40}', source['sha']),
         'missing/invalid installation source pin')
    need(type(source.get('published')) is bool, 'missing installation source publication status')
    managed = [str(root / name) for name in ('START.md', 'DIRECTOR.md', 'OPERATIONS.md', 'startup_check.py')]
    managed_paths = {safe(project, value).relative_to(project).as_posix() for value in managed}
    need(not Path(hook_source).is_absolute(), 'hook source must be project-relative')
    hook_relative = safe(project, hook_source).relative_to(project).as_posix()
    route = ['AGENTS.md', *managed, *guards, hook_source]
    if backend_contract:
        route.append(backend_contract)
    selected = {}
    for value in route:
        path = safe(project, value)
        selected.setdefault(path.relative_to(project).as_posix(), path)
    need(len(selected) <= 20, 'too many selected startup guards')
    checked = []
    snapshots = []
    hook = None
    for relative, path in selected.items():
        expected = baseline(receipt, relative, required=relative in managed_paths)
        data = read(path, MAX_FILE, total)
        digest = hashlib.sha256(data).hexdigest()
        if relative in managed_paths:
            need(digest == expected, 'startup baseline mismatch: ' + relative)
        else:
            text = data.decode('utf-8')
            snapshots.append({'path': relative, 'snapshot': 'not_recorded' if expected is None else
                              'unchanged' if digest == expected else 'changed'})
        if relative == hook_relative:
            hook = startup_hook(data.decode('utf-8'), (root / 'START.md').relative_to(project).as_posix(), relative)
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
        if config['record_mode'] == 'tracked':
            store = config.get('request_store')
            need(isinstance(store, dict) and type(store.get('schema_version')) is int and store['schema_version'] == 2, 'unsupported tracked-store schema header')
            need(store.get('format') in {'director-request-bundles', 'request-bundles'}, 'unknown tracked-store format; use the actual project backend contract')
            need(isinstance(store.get('project_id'), str) and re.fullmatch('PROJ-[0-9a-f]{32}', store['project_id']), 'missing/invalid configured project identity')
            expected = expect_project_id or receipt.get('project_id')
            if expected is not None:
                need(store['project_id'] == expected, 'configured project identity differs from selected project')
        backend = {'kind': 'configuration header', 'path': config_path.relative_to(project).as_posix(),
                   'schema_version': config['schema_version'], 'record_mode': config['record_mode']}
    return {'status': 'evidence_matched', 'scope': 'managed evidence and marked route structure checked; current project instruction evaluation still required',
            'source_sha': source['sha'], 'source_published': source['published'],
            'source_local_delta': source.get('local_delta', 'not recorded'),
            'receipt': receipt_path.relative_to(project).as_posix(), 'checked_paths': checked,
            'startup_hook': hook, 'project_instruction_snapshots': snapshots,
            'actor_must_confirm': ['resolved Project Director role and complete startup reads', 'all actual selected role/shared guards included', 'authoritative canonical backend and config/contract binding',
                                  'effective host-loaded route and complete current project instructions, including conflicts outside the hook'],
            'backend': backend, 'bytes_read': total[0],
            'not_proved': ['instruction consumption or role authority', 'ledger/history integrity',
                           'native host behavior or effective model', 'human acceptance or live execution',
                           'semantic compatibility of project instructions']}


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
        result = {'status': 'blocked', 'scope': 'bounded local operational evidence only', 'gap': str(error)[:600]}
        code = 1
    output = json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    if len(output.encode()) > 4096:
        output = json.dumps({'status':'blocked','gap':'startup result exceeds output bound'}, separators=(',', ':'))
        code = 1
    print(output)
    return code


if __name__ == '__main__':
    raise SystemExit(main())

"""Development-only load inventory, not an instruction parser or installed runtime.

The reviewed scenario sets are explicit. Current capability destinations come from
the actual bootstrap table; tests separately check expected policy coverage and
package link closure. This cannot establish an agent read or followed a protocol.
"""
import argparse
import json
import math
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PATTERN = ROOT / 'pattern'
BASELINE = '28e7bb9'
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
DIRECTOR_ACTION = {
    'engine/DIRECTION.md', 'engine/MODELS.md', 'engine/STATE.md',
    'engine/ROLES.md', 'engine/ASSIGNMENT.md', 'engine/IDENTITIES.md',
}
BASE = {'PATTERN.md', 'engine/PATTERN.md'}
STARTUP = {
    'director': BASE | {'engine/DIRECTOR.md'},
    'request-manager': BASE | {'engine/REQUEST_MANAGER.md'},
    'analysis-worker': BASE | {'engine/ANALYSIS.md', 'engine/WORKER.md'},
}
# Stable project fixture bytes are intentionally separate from engine/package size.
PROJECT = '''# Fixture project
Canonical role index: ROLE_INDEX.md
Authority: AUTHORITY.md; no external publication without user authorization.
Mode: lean; existing tracker remains canonical.
Recorder: indexed shared responsibility; direct only if supported, else via assigner.
State/activity/identity roster: existing tracker and activity.md; one shared cursor.
Capability and authority policy: durable project policy; resolve current host controls at use.
'''
INDEX = '''# Fixture canonical index
Shared guardrails: [authority](AUTHORITY.md).
director: [Director](engine/DIRECTOR.md), Role: director.
request-manager: [Request Manager](engine/REQUEST_MANAGER.md), Role: director.
analysis-worker: [Analysis](engine/ANALYSIS.md), Role: worker.
recorder: [Recorder](engine/RECORDER.md), Role: worker.
reviewer: [Reviewer](roles/reviewer.md), Role: worker.
'''
AUTHORITY = 'Keep the existing tracker canonical. No publication without user authorization.\n'


def capability_protocols(root=PATTERN):
    """Read only the explicit before-use table; ordinary links are not load edges."""
    text = (root / 'engine/PATTERN.md').read_text()
    section = text.split('## Required capability protocols\n', 1)[1]
    result = {}
    for line in section.splitlines():
        if not line.startswith('| ') or line.startswith('| Capability '):
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) != 3:
            continue
        name, trigger, protocols = cells
        paths = set()
        for link in LINK.findall(protocols):
            if '://' in link:
                continue
            paths.add((Path('engine') / link.split('#')[0]).as_posix())
        result[name] = {'trigger': trigger, 'paths': paths}
    return result


def source_bytes(name, revision=None):
    if revision:
        return subprocess.run(['git', 'show', f'{revision}:pattern/{name}'],
                              cwd=ROOT, check=True, capture_output=True).stdout
    return (PATTERN / name).read_bytes()


def inventory(tokens=False):
    encode = None
    if tokens:
        import tiktoken  # Optional reporting aid, never an installed dependency.
        encode = tiktoken.get_encoding('cl100k_base').encode
    rows = []
    for role, paths in STARTUP.items():
        for version in ('baseline', 'candidate'):
            selected = paths | (DIRECTOR_ACTION if role != 'analysis-worker' and version == 'baseline' else set())
            data = [source_bytes(p, BASELINE if version == 'baseline' else None) for p in sorted(selected)]
            context = [INDEX.encode(), AUTHORITY.encode()]
            if role != 'analysis-worker':
                context.append(PROJECT.encode())
            row = {'role': role, 'version': version,
                   'shared_package_files': len(data), 'shared_package_bytes': sum(map(len, data)),
                   'project_fixture_bytes': sum(map(len, context)),
                   'dependency_stages': 5 if role != 'analysis-worker' and version == 'baseline' else 4,
                   # One file/chunk per response, 12 KB illustrative text payload.
                   # Framing/escaping/token limits must still be chosen on the host.
                   'responses_at_12000_bytes': sum(math.ceil(len(x) / 12000) for x in data + context)}
            if encode:
                row['shared_cl100k_tokens'] = sum(len(encode(x.decode())) for x in data)
                row['project_cl100k_tokens'] = sum(len(encode(x.decode())) for x in context)
            rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tokens', action='store_true', help='Use optional existing tiktoken for cl100k proxy counts')
    args = parser.parse_args()
    print(json.dumps({'baseline': BASELINE, 'scope': 'declared static file sets; no behavior or latency measurement',
                      'rows': inventory(args.tokens)}, indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Opt-in raw-byte inventory for a caller-resolved instruction chain; no host probe."""
import argparse
import codecs
import hashlib
import json
import os
from pathlib import Path
import stat
import sys

MAX_SPEC = 128_000
MAX_FILE = 1_000_000
MAX_TOTAL = 4_000_000
MAX_CHAIN = 128
MAX_CAP = 2**63 - 1
MIN_OUTPUT = 256
MAX_OUTPUT = 262_144
LIMITS = [
    'Caller resolves the actual host route, overrides, order and cap evidence.',
    'Raw file bytes exclude host framing and global versus project instruction counters.',
    'Predicted intervals are byte slices, not valid or semantically complete instructions.',
    'No native admission, returned-read coverage, consumption or compaction restoration is proved.',
    'Unknown provenance ignores numeric caps; default caps are conditional; null caps yield unknown predictions.',
    'Boundary fit covers caller assertions only; null or zero boundaries do not establish required instruction coverage.',
    'Bounds: 128 files, 1000000 bytes/file, 4000000 chain bytes, 128000 spec bytes; no content is returned.',
]


class InputError(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise InputError(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def signature(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def open_directory(path):
    """Walk from / using directory descriptors; never follow a symlink."""
    path = Path(os.path.abspath(path))
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parts[1:]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except BaseException:
        os.close(fd)
        raise


def open_selected(root_fd, relative):
    fd = os.dup(root_fd)
    try:
        parts = relative.split('/')
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        # NONBLOCK avoids hanging on a substituted FIFO before the regular-file check.
        return os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
    finally:
        os.close(fd)


def measure(root_fd, relative, limit, remaining, keep=False):
    fd = open_selected(root_fd, relative)
    try:
        before = os.fstat(fd)
        need(stat.S_ISREG(before.st_mode), 'selected path must be a regular file')
        need(before.st_size <= min(limit, remaining), 'selected bytes exceed read bound')
        digest = hashlib.sha256()
        decoder = codecs.getincrementaldecoder('utf-8')()
        chunks, size = [], 0
        while True:
            chunk = os.read(fd, min(65_536, limit + 1 - size))
            if not chunk:
                break
            size += len(chunk)
            need(size <= min(limit, remaining), 'selected bytes exceed read bound')
            digest.update(chunk)
            decoder.decode(chunk)
            if keep:
                chunks.append(chunk)
        decoder.decode(b'', final=True)
        need(signature(before) == signature(os.fstat(fd)) and size == before.st_size,
             'selected file changed during measurement')
        return size, digest.hexdigest(), signature(before), b''.join(chunks)
    finally:
        os.close(fd)


def load_spec(path):
    path = Path(os.path.abspath(path))
    fd = open_directory(path.parent)
    try:
        _, _, _, data = measure(fd, path.name, MAX_SPEC, MAX_SPEC, keep=True)
    finally:
        os.close(fd)
    value = json.loads(data, object_pairs_hook=unique,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON value')))
    need(isinstance(value, dict) and set(value) == {'schema', 'chain', 'cap', 'evidence'}, 'invalid spec keys')
    need(type(value['schema']) is int and value['schema'] == 1, 'unsupported spec schema')
    chain = value['chain']
    need(isinstance(chain, list) and 0 < len(chain) <= MAX_CHAIN, 'invalid or oversized chain')
    seen = set()
    for item in chain:
        need(isinstance(item, dict) and set(item) == {'path', 'required_through_bytes'}, 'invalid chain entry')
        name, boundary = item['path'], item['required_through_bytes']
        need(isinstance(name, str) and 0 < len(name.encode('utf-8')) <= 512 and
             not name.startswith('/') and all(p not in {'', '.', '..'} for p in name.split('/')) and
             not any(ord(c) < 32 for c in name), 'unsafe project-relative path')
        need(name not in seen, 'duplicate selected path')
        seen.add(name)
        need(boundary is None or type(boundary) is int and boundary >= 0, 'invalid required boundary')
    cap = value['cap']
    need(isinstance(cap, dict) and set(cap) == {'bytes', 'provenance'}, 'invalid cap keys')
    need(cap['bytes'] is None or type(cap['bytes']) is int and 0 < cap['bytes'] <= MAX_CAP, 'invalid cap bytes')
    need(cap['provenance'] in ('effective', 'default', 'unknown'), 'invalid cap provenance')
    need(isinstance(value['evidence'], str) and value['evidence'].strip() and
         len(value['evidence'].encode('utf-8')) <= 2048, 'missing or oversized caller evidence locator')
    return value


def check(root, spec):
    root_fd = open_directory(root)
    try:
        cap = spec['cap']
        budget = cap['bytes'] if cap['provenance'] != 'unknown' else None
        rows, snapshots, total = [], [], 0
        for item in spec['chain']:
            name, boundary = item['path'], item['required_through_bytes']
            size, digest, snapshot, _ = measure(root_fd, name, MAX_FILE, MAX_TOTAL - total)
            need(boundary is None or boundary <= size, 'required boundary exceeds selected file')
            counted = None if budget is None else min(size, max(0, budget - total))
            prediction = 'unknown' if counted is None else (
                'read' if counted == size else 'omitted' if counted == 0 else 'truncated')
            rows.append({'path': name, 'sha256': digest, 'raw_bytes': size,
                         'cumulative_raw_bytes': total + size,
                         'cumulative_counted_bytes': None if budget is None else min(total + size, budget),
                         'predicted_raw_budget': {'status': prediction,
                             'read_interval': None if counted is None else [0, counted],
                             'omitted_interval': None if counted is None else [counted, size]},
                         'required_through_bytes': boundary,
                         'required_boundary_fits': None if boundary is None or budget is None else total + boundary <= budget})
            snapshots.append((name, snapshot))
            total += size
        # A later file read must not conceal changes to an earlier selected file.
        for name, snapshot in snapshots:
            fd = open_selected(root_fd, name)
            try:
                need(signature(os.fstat(fd)) == snapshot, 'selected file changed during measurement')
            finally:
                os.close(fd)
        asserted = [r['required_boundary_fits'] for r in rows if r['required_through_bytes']]
        return {'schema': 1, 'status': 'measured', 'actual_admission': 'unqualified',
                'declared_budget': 'unknown' if budget is None else 'under' if total <= budget else 'over',
                'cap': cap, 'prediction_basis': 'unknown' if budget is None else
                    'conditional_default' if cap['provenance'] == 'default' else 'declared_effective',
                'evidence': spec['evidence'], 'total_raw_bytes': total,
                'total_counted_bytes': None if budget is None else min(total, budget),
                'asserted_required_boundaries_fit': None if not asserted or budget is None else all(asserted),
                'asserted_boundary_count': len(asserted),
                'unasserted_path_count': len(rows) - len(asserted),
                'interval_convention': '[start,end) raw byte offsets within each file',
                'files': rows, 'limits': LIMITS}
    finally:
        os.close(root_fd)


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise InputError('invalid arguments; use --help')


def main(argv=None):
    output_limit = 4096
    try:
        parser = Parser(description=__doc__, epilog='Unknown cap provenance ignores numeric caps; default caps are conditional. '
                        'Use only at a selected installation/update qualification, not as a startup duty.')
        parser.add_argument('--root', required=True, type=Path, help='Explicit project root')
        parser.add_argument('--spec', required=True, type=Path, help='Exact caller-resolved schema-1 JSON spec')
        parser.add_argument('--max-output-bytes', required=True, type=int, help='Complete JSON output bound, 256..262144')
        args = parser.parse_args(argv)
        need(MIN_OUTPUT <= args.max_output_bytes <= MAX_OUTPUT, 'output bound must be 256..262144')
        output_limit = args.max_output_bytes
        result = check(args.root, load_spec(args.spec))
        code = 0
    except InputError as error:
        result = {'status': 'blocked', 'actual_admission': 'unqualified', 'gap': str(error)}
        code = 1
    except (ValueError, OSError, TypeError, KeyError, UnicodeError, RecursionError):
        # Never echo source bytes, JSON parser excerpts or user-selected path content.
        result = {'status': 'blocked', 'actual_admission': 'unqualified',
                  'gap': 'invalid, inaccessible, unsafe, changing or oversized input; check spec and read bounds'}
        code = 1
    output = json.dumps(result, ensure_ascii=True, separators=(',', ':')) + '\n'
    if len(output.encode('utf-8')) > output_limit:
        output = json.dumps({'status': 'blocked', 'actual_admission': 'unqualified',
                             'gap': 'complete report exceeds output bound'}, separators=(',', ':')) + '\n'
        code = 1
    print(output, end='')
    return code


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Stable interface 1 entrypoint; implementation belongs to replaceable engine/."""
import importlib.util
from pathlib import Path
import sys

# Importing the engine must not create bytecode cache inside replaceable payload.
sys.dont_write_bytecode = True
_ROOT = Path(__file__).resolve().parents[1]
_IMPL = _ROOT / "engine/tools/requests.py"
_SPEC = importlib.util.spec_from_file_location("director_engine_requests", _IMPL)
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)
globals().update({k: v for k, v in vars(_MODULE).items() if not k.startswith("_")})
if __name__ == "__main__":
    if "--team" not in sys.argv[1:]:
        sys.argv[1:1] = ["--team", str(_ROOT)]
    sys.exit(_MODULE.main())

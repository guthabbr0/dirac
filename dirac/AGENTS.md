# dirac

This package is the modular runtime. Keep `__init__.py` boring and keep shared domain values in `types.py` only.

Each subpackage owns one boundary and exposes a small public contract. Do not create new cross-module shortcuts here. If two modules need to communicate, define a typed value or port in the owner module and inject it from `runtime`.

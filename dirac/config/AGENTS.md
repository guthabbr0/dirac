# dirac/config

Owns: static files, environment values, typed settings, secret presence.

Exposes: BaseConfig and concrete file-backed config readers.

Must not import or control: runtime storage internals, provider calls, command parsing.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

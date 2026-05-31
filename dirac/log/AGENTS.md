# dirac/log

Owns: structured events, redaction, console controls, sinks.

Exposes: BaseLog plus console/no-op implementations.

Must not import or control: business decisions, provider routing, memory storage.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

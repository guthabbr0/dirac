# dirac/command

Owns: deterministic command parsing and command execution.

Exposes: parse_command and CommandService.

Must not import or control: provider calls before permission checks.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

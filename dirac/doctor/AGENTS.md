# dirac/doctor

Owns: maintenance, repair, validation, recovery ports.

Exposes: doctor CLI and explicit repair methods.

Must not import or control: normal operator API shortcuts or secret exposure.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

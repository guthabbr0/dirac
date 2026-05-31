# dirac/api

Owns: authenticated HTTP routes and DTOs.

Exposes: create_app and API contracts.

Must not import or control: frontend code, provider-specific HTTP internals.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

# dirac/permission

Owns: authorization, scope decisions, blocked users, capability gates.

Exposes: PermissionService decisions.

Must not import or control: provider clients, memory storage internals, UI code.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

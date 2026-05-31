# dirac/tool

Owns: tool definitions, scoped visibility, execution, result normalization.

Exposes: ToolRegistry and ToolExecutor contracts.

Must not import or control: provider HTTP internals, raw Discord permissions.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

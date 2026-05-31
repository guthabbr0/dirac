# dirac/discord

Owns: Discord adapter, event normalization, delivery, identity helpers.

Exposes: adapter DTOs and delivery methods.

Must not import or control: provider routing internals, memory storage internals.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

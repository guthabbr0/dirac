# dirac/memory

Owns: durable memory and recent visible event access through one contract.

Exposes: BaseMemory, memory contracts, memory tool facade.

Must not import or control: provider clients, UI code, direct storage leaks.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

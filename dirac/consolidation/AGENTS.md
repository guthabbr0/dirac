# dirac/consolidation

Owns: quiet-phase memory assimilation and audits.

Exposes: ConsolidationService and audit DTOs.

Must not import or control: ordinary task scheduling internals, Discord SDK objects.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

# dirac/context

Owns: model-facing context assembly and filters.

Exposes: ContextAssembler and filter helpers.

Must not import or control: provider HTTP, storage handles, Discord SDK objects.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

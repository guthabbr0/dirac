# dirac/provider

Owns: provider routing, request translation, HTTP calls, fake clients.

Exposes: BaseProviderClient implementations.

Must not import or control: Discord details, memory internals, command permissions.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

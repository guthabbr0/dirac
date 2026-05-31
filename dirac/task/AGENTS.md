# dirac/task

Owns: periodic task definitions, loose due-task selection, attempts.

Exposes: TaskService and LooseTaskScheduler.

Must not import or control: WebUI implementation, provider-specific HTTP payloads.

Keep this module small. Change public contracts before reaching into another module. Tests for this module belong under `tests/` and should exercise behavior through the public contract.

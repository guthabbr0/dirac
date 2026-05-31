from __future__ import annotations

from dirac.provider.base import BaseProviderClient
from dirac.types import ProviderRequest, ProviderResponse, TaskDefinition


class TaskService:
    def __init__(self, provider: BaseProviderClient) -> None:
        self.provider = provider

    async def run_attempt(self, task: TaskDefinition, *, model: str) -> ProviderResponse:
        request = ProviderRequest(
            messages=[{"role": "user", "content": task.prompt}],
            model=model,
            scope=task.scope,
            source="task",
            metadata={"task_id": task.task_id, "runtime_kind": task.runtime_kind},
        )
        return await self.provider.chat(request)

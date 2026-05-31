from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dirac.types import Scope


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    name: str
    description: str
    definition: dict[str, Any]
    enabled: bool = True


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        self._tools[tool.name] = tool

    async def enabled_for_scope(self, scope: Scope) -> list[ToolDefinition]:
        _ = scope
        return [tool for tool in self._tools.values() if tool.enabled]

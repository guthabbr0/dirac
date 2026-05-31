from __future__ import annotations

from dirac.permission.service import PermissionService
from dirac.types import Scope

from .parser import ParsedCommand


class CommandService:
    def __init__(self, permissions: PermissionService) -> None:
        self.permissions = permissions

    async def handle(self, command: ParsedCommand, *, user_id: str, scope: Scope) -> str:
        decision = await self.permissions.can_run_command(user_id, command.name, scope)
        if not decision.allowed:
            return decision.reason
        if command.name == "help":
            return "Dirac command service is alive. Add command handlers behind this boundary."
        return "unknown_command"

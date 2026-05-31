from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from dirac.types import Scope


@dataclass(frozen=True, slots=True)
class DiscordEvent:
    message_id: str
    author_id: str
    author_name: str
    content: str
    scope: Scope
    reply_to_id: str | None = None


class BaseDiscordAdapter(ABC):
    @abstractmethod
    async def send_text(self, scope: Scope, text: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def record_visible_event(self, event: DiscordEvent) -> None:
        raise NotImplementedError

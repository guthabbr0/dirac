from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ProviderSettings:
    name: str
    kind: str
    base_url: str
    model: str
    api_key: str = ""
    timeout_s: float = 120.0
    params: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class DiscordSettings:
    token: str
    root_operator_ids: tuple[str, ...] = ()
    selfbot_risk_acknowledged: bool = False


@dataclass(frozen=True, slots=True)
class ApiSettings:
    host: str = "127.0.0.1"
    port: int = 8765
    auth_token: str = ""


class BaseConfig(ABC):
    @abstractmethod
    def provider_settings(self, name: str = "default") -> ProviderSettings:
        raise NotImplementedError

    @abstractmethod
    def discord_settings(self) -> DiscordSettings:
        raise NotImplementedError

    @abstractmethod
    def api_settings(self) -> ApiSettings:
        raise NotImplementedError

    @abstractmethod
    def logging_settings(self) -> dict[str, Any]:
        raise NotImplementedError


BaseVirtualConfig = BaseConfig

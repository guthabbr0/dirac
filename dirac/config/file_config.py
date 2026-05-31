from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .base import ApiSettings, BaseConfig, DiscordSettings, ProviderSettings


@dataclass(frozen=True, slots=True)
class FileConfig(BaseConfig):
    data: dict[str, Any]

    def provider_settings(self, name: str = "default") -> ProviderSettings:
        providers = self.data.get("providers", {})
        raw = providers.get(name, {}) if isinstance(providers, dict) else {}
        return ProviderSettings(
            name=name,
            kind=str(raw.get("kind", "ollama")),
            base_url=str(raw.get("base_url", "https://ollama.com")).rstrip("/"),
            model=str(raw.get("model", "llama3.2")),
            api_key=str(raw.get("api_key", "")),
            timeout_s=float(raw.get("timeout_s", 120.0)),
            params=dict(raw.get("params", {})) if isinstance(raw.get("params"), dict) else {},
        )

    def discord_settings(self) -> DiscordSettings:
        raw = self.data.get("discord", {})
        ids = tuple(str(item) for item in raw.get("root_operator_ids", []) if str(item))
        return DiscordSettings(
            token=str(raw.get("token", "")),
            root_operator_ids=ids,
            selfbot_risk_acknowledged=bool(raw.get("i_understand_selfbot_risk", False)),
        )

    def api_settings(self) -> ApiSettings:
        raw = self.data.get("api", {})
        return ApiSettings(
            host=str(raw.get("host", "127.0.0.1")),
            port=int(raw.get("port", 8765)),
            auth_token=str(raw.get("auth_token", "")),
        )

    def logging_settings(self) -> dict[str, Any]:
        raw = self.data.get("logging", {})
        return dict(raw) if isinstance(raw, dict) else {}


def load_config(path: str | Path) -> FileConfig:
    with Path(path).open("rb") as handle:
        return FileConfig(tomllib.load(handle))

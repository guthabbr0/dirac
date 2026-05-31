from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


COMMON_PARAMETER_KEYS = {
    "temperature",
    "top_p",
    "top_k",
    "max_tokens",
    "presence_penalty",
    "frequency_penalty",
    "reasoning",
    "reasoning_effort",
    "timeout_s",
    "tools_enabled",
    "streaming",
    "response_format",
    "seed",
}


@dataclass(frozen=True, slots=True)
class ParameterTranslation:
    sent: dict[str, Any] = field(default_factory=dict)
    ignored: dict[str, Any] = field(default_factory=dict)


def split_supported_params(params: dict[str, Any], supported: set[str]) -> ParameterTranslation:
    sent: dict[str, Any] = {}
    ignored: dict[str, Any] = {}
    for key, value in dict(params or {}).items():
        if key in supported:
            sent[key] = value
        elif key in COMMON_PARAMETER_KEYS:
            ignored[key] = value
    return ParameterTranslation(sent=sent, ignored=ignored)

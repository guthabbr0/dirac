from __future__ import annotations

import re
from typing import Any


SNOWFLAKE_RE = re.compile(r"(?<!\d)(\d{15,22})(?!\d)")


def normalize_snowflake(value: Any) -> str:
    text = str(value or "").strip()
    for pattern in (r"<@!?(\d{15,22})>", r"<#(\d{15,22})>"):
        match = re.fullmatch(pattern, text)
        if match:
            return match.group(1)
    match = SNOWFLAKE_RE.search(text)
    return match.group(1) if match else text


def collect_snowflakes(*values: Any, limit: int = 40) -> list[str]:
    seen: list[str] = []
    for value in values:
        if isinstance(value, (list, tuple, set)):
            candidates = collect_snowflakes(*value, limit=limit)
        else:
            candidates = SNOWFLAKE_RE.findall(str(value or ""))
        for candidate in candidates:
            if candidate not in seen:
                seen.append(candidate)
            if len(seen) >= limit:
                return seen
    return seen

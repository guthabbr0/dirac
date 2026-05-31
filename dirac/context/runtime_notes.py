from __future__ import annotations

from datetime import datetime, timezone


TOOL_TURN_STATE_PLACEHOLDER = "{{DIRAC_TOOL_TURN_STATE}}"


def current_time_note() -> str:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    return f"Trusted runtime note: current UTC time is {now}."


def render_tool_turn_state(surface: str, turn_number: int, total_turns: int) -> str:
    total = max(1, int(total_turns or 1))
    turn = max(1, min(int(turn_number or 1), total))
    return f"[[ {surface.upper()} TOOL ROUND {turn}/{total} ]]"

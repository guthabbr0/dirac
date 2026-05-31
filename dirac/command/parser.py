from __future__ import annotations

import re
import shlex
from dataclasses import dataclass


COMMAND_RE = re.compile(r"^!([A-Za-z][\w-]*)(?:\s+(.*))?$", re.S)


@dataclass(frozen=True, slots=True)
class ParsedCommand:
    name: str
    args: tuple[str, ...]
    scope_modifier: str | None = None


def parse_command(text: str) -> ParsedCommand | None:
    match = COMMAND_RE.match(text.strip())
    if not match:
        return None
    lexer = shlex.shlex((match.group(2) or "").strip(), posix=True)
    lexer.whitespace_split = True
    lexer.commenters = ""
    parts = list(lexer)
    scope_modifier = None
    if parts and parts[-1] == "*":
        scope_modifier = "global"
        parts = parts[:-1]
    elif parts and re.fullmatch(r"@\S+", parts[-1]):
        scope_modifier = parts[-1][1:]
        parts = parts[:-1]
    return ParsedCommand(match.group(1).lower(), tuple(parts), scope_modifier)

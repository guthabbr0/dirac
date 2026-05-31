from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dirac doctor maintenance CLI")
    parser.add_argument("command", nargs="?", default="status", choices=["status"])
    args = parser.parse_args(argv)
    if args.command == "status":
        print("doctor skeleton ok")
    return 0

#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers (make.fun entry).

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic, no network,
no model calls, exits 0.
"""
import os
import sys

LINE = "The bug that only wakes on Fridays already knows your weekend plans."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

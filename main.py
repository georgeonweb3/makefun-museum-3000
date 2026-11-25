#!/usr/bin/env python3
"""Museum of the Year 3000 — one museum label from the year 3000.

The line is the whole entry: a deadpan label beside an ordinary object from
today (birthday candles). The year-3000 curator misreads the ritual — small
fires stuck in a cake, blown out while singing — as an ageing rite, which is
true (we really do it) and absurd (it ages no one).
"""

import os

LINE = "Birthday candles, c. 2024. Small fires, stuck in a cake and blown out while singing. Scholars believe the ritual aged the eater by one year."


def validate(line: str) -> None:
    """The gate: 1 to 200 characters of UTF-8 text, not only whitespace."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    # A real museum label names the object and dates it.
    if ", c. 20" not in line:
        raise SystemExit("line must read as a dated museum label")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()

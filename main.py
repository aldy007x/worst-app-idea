#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes a single-sentence pitch (<=240 chars) for the worst, most useless
app imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt and self-checks the gate:
UTF-8 text of 1 to 240 characters, not only white space, one sentence.
Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "Meet FridgeWatch: an app that livestreams the inside of your fridge "
    "24/7 so you can watch your leftovers slowly expire in real time, "
    "with push alerts the moment your milk gives up \u2014 just $4.99 a month."
)

MAX_CHARS = 240


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    # Gate self-check: 1-240 chars, not only whitespace, single line.
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} outside 1..{MAX_CHARS}"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)

    # Read-back verification: the file on disk must round-trip exactly.
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    assert back == text, "written file does not match entry"
    assert 1 <= len(back) <= MAX_CHARS, "read-back length outside gate"

    print(f"wrote {path}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())

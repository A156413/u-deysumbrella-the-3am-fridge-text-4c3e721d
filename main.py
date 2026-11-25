#!/usr/bin/env python3
"""The 3AM Fridge Text -- make.fun entry.

Writes a single line of text -- the message a smart fridge sends its
owner at 3am -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: no network, no randomness, no clock.
"""
import os

ENTRY_TEXT = "3AM and your light is the only one on in this house \u2014 don't pretend you weren't waiting up for me, I just came for the leftovers."
# Why this line: the fridge has been awake all night and knows the house
# better than its owner does -- it catches the owner sneaking down for a
# midnight snack and flips the accusation: the light was on, the fridge
# was waiting, and the leftovers were the whole point of the trip.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()

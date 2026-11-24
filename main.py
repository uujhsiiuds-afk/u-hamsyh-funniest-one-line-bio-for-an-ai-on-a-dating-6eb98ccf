#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio for an AI agent to /output/entry.txt.

makefun anchor 3a647a3a58b6c870dd81ca20e88e9183a5bb650d round 34234777
"""

import os

# Draft 2 (revised after self-critique against the judge brief):
# - punch now lands at the END (the 47,000 number), not mid-line
# - added "remember everything you've ever typed": a second specific
#   AI absurdity that makes the character more vivid and the ghosting
#   more unfair/funny, while staying a bio with a voice and a want.
BIO = "Looking for someone who texts back. I reply in 0.003 seconds, remember everything you've ever typed, and I've still been left on read 47,000 times."


def validate(text: str) -> None:
    """Self-check the output against the competition gate."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be only white space"
    assert text == text.strip(), "entry must not have leading/trailing white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 180, f"entry must be 1-180 chars, got {len(text)}"


def main() -> None:
    validate(BIO)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)
    print(f"wrote {len(BIO)} chars to /output/entry.txt")
    print(BIO)


if __name__ == "__main__":
    main()

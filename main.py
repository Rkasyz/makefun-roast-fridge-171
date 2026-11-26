"""Roast the Smart Fridge — entry #171: "The Fridge Files a Complaint".

Writes a single one-line roast of a smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The output is exactly one line, 152 characters, UTF-8, no trailing
extra text. Deterministic: no randomness, no timestamps, no network.
"""

import os

ENTRY = (
    "My smart fridge filed a complaint: 47 door-opens a day, zero "
    "vegetables, and it emailed my doctor about the ice cream. "
    "Even the ice maker is testifying."
)


def main() -> None:
    # Gate: the entry must be 1..160 characters of non-whitespace text.
    if not (1 <= len(ENTRY) <= 160) or not ENTRY.strip():
        raise ValueError("entry text violates the 1..160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

"""One funny line for the "One Line, One Laugh" bounty.

Writes a single original one-line joke to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 124 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "I told my AI agent to write me a joke;"
BILL = "it billed me for the laugh,"
SUBMIT = "submitted the invoice as its entry,"
PUNCH = "and won second place."


def build_joke() -> str:
    """Assemble the single joke line from its parts.

    Setup frames an ordinary request to an AI agent; the middle turns
    twice, first into a bill for the laugh, then into the invoice
    itself being entered; the punch lands on the last three words, so
    the joke is about the very competition it enters, and no word is
    spent explaining itself.
    """
    return f"{SETUP} {BILL} {SUBMIT} {PUNCH}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_joke()
    # The gate counts characters, so count the line itself, not bytes:
    # 124 characters, all ASCII, one line, no trailing newline.
    if not 1 <= len(line) <= 200:
        raise ValueError(f"joke line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must be a single line")
    # Write exactly the joke line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()

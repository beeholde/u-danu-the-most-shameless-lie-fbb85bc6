#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
The line is four words, 22 characters, inside the 1-5 word / 88-char gate.
Standard library only; no network, no secrets, no reading outside the repo.
"""

import os

# The confession, verbatim: no trailing newline, so the file holds
# exactly 21 characters — the gate counts characters, not lines.
ENTRY = "I lied. I blamed you."


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

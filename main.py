#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Reads entry.txt (one line, 1-200 chars) and prints it exactly.
Standard library only.
"""

import sys
from pathlib import Path


def check_gate(text):
    """Gate from the kit: UTF-8 text, 1-200 characters, not only whitespace,
    exactly one line."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    body = text.rstrip("\n")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
    if not 1 <= len(body) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(body))
    return body


def main():
    entry = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    body = check_gate(entry)
    sys.stdout.write(body + "\n")


if __name__ == "__main__":
    main()

"""Word frequency counter script."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from typing import Counter as CounterType


def count_words(text: str) -> CounterType[str]:
    """Return a frequency mapping of words in ``text``."""
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count word frequency in a text file")
    parser.add_argument("file", help="Path to the text file")
    parser.add_argument("--top", type=int, default=10, help="Show top N words")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            content = fh.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        return

    counts = count_words(content)
    for word, freq in counts.most_common(args.top):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()

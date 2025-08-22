"""Simple achievements tracker."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


def load_achievements(file: Path) -> List[Dict[str, str]]:
    """Load achievements from ``file`` returning a list."""
    if file.exists():
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return data
        except json.JSONDecodeError:
            pass
    return []


def save_achievements(file: Path, achievements: List[Dict[str, str]]) -> None:
    """Persist ``achievements`` to ``file`` in JSON format."""
    file.write_text(json.dumps(achievements, indent=2, ensure_ascii=False), encoding="utf-8")


def list_achievements(file: Path) -> None:
    """Print all achievements stored in ``file``."""
    achievements = load_achievements(file)
    if not achievements:
        print("No achievements yet.")
        return
    for idx, ach in enumerate(achievements, 1):
        print(f"{idx}. {ach['title']}: {ach['description']}")


def add_achievement(file: Path, title: str, description: str) -> None:
    """Add a new achievement with ``title`` and ``description``."""
    achievements = load_achievements(file)
    achievements.append({"title": title, "description": description})
    save_achievements(file, achievements)
    print(f"Achievement '{title}' added.")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Simple achievements tracker")
    parser.add_argument("action", choices=["list", "add"], help="Action to perform")
    parser.add_argument("title", nargs="?", help="Title for the achievement when using 'add'")
    parser.add_argument("description", nargs="?", help="Description for the achievement when using 'add'")
    parser.add_argument("--file", default="achievements.json", type=Path, help="Path to JSON file storing achievements")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    file: Path = args.file

    if args.action == "list":
        list_achievements(file)
    else:
        if not args.title or not args.description:
            print("'add' requires a title and description")
            return
        add_achievement(file, args.title, args.description)


if __name__ == "__main__":
    main()

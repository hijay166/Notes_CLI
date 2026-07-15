"""Simple JSON-backed storage for notes.

Each note is a dict with the shape:

    {
        "id": int,
        "text": str,
        "created_at": str,   # ISO 8601
        "deleted": bool,     # soft-delete flag
        "deleted_at": str | None,  # ISO 8601, set when deleted=True
    }
"""
import json
from pathlib import Path


def load_notes(path: str) -> list:
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(path: str, notes: list) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

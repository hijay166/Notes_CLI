import argparse
from datetime import datetime

from .cleanup import purge_old
from .storage import load_notes, save_notes


def main():
    parser = argparse.ArgumentParser(prog="notes")
    sub = parser.add_subparsers(dest="command", required=True)

    purge = sub.add_parser("purge", help="Run the retention cleanup job")
    purge.add_argument("--db", default="notes.json")
    purge.add_argument("--retention-days", type=int, default=30)

    args = parser.parse_args()

    if args.command == "purge":
        notes = load_notes(args.db)
        remaining = purge_old(notes, args.retention_days, now=datetime.utcnow())
        save_notes(args.db, remaining)
        print(f"Purge complete. {len(notes) - len(remaining)} note(s) removed, "
              f"{len(remaining)} remaining.")


if __name__ == "__main__":
    main()

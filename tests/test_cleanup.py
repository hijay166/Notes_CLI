from datetime import datetime, timedelta

from notes.cleanup import purge_old


def _iso(dt):
    return dt.isoformat()


def test_purge_respects_retention_window():
    now = datetime(2026, 1, 1)

    old_deleted = {
        "id": 1,
        "text": "old deleted note",
        "created_at": _iso(now - timedelta(days=400)),
        "deleted": True,
        "deleted_at": _iso(now - timedelta(days=100)),
    }
    recent_deleted = {
        "id": 2,
        "text": "recently deleted note",
        "created_at": _iso(now - timedelta(days=10)),
        "deleted": True,
        "deleted_at": _iso(now - timedelta(days=5)),
    }

    result = purge_old([old_deleted, recent_deleted], retention_days=30, now=now)
    ids = {n["id"] for n in result}

    assert ids == {2}
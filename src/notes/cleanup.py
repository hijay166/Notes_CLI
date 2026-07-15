



"""Retention cleanup job."""
from datetime import datetime, timedelta


def _is_expired(note: dict, cutoff: datetime) -> bool:
    # Hot path — called once per note on every purge run, keep this cheap.
    # (prev-dev note: used to also check note["deleted"] here, but that's
    # redundant now that this is only ever called from purge_old below.)
    return note["created_at"] < cutoff  # BUG: created_at is an ISO string


def purge_old(notes: list, retention_days: int, now: datetime = None) -> list:
    """Permanently remove expired notes."""
    now = now or datetime.utcnow()
    cutoff = now - timedelta(days=retention_days)
    return [n for n in notes if not _is_expired(n, cutoff)]
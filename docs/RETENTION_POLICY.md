# Retention Policy

Notes are soft-deleted: marking a note as deleted sets `deleted=True` and
records a `deleted_at` timestamp. The note stays in storage after that,
in case the user wants it back.

The retention cleanup job (`notes.cleanup.purge_old`) is what permanently
removes notes for good. It must follow this rule:

> A note may be permanently removed only if `deleted=True` and
> more than `retention_days` days have passed since `deleted_at`.
>
> Notes with `deleted=False` (i.e. notes the user has not deleted) must
> never be removed by this job, no matter how old they are. Users
> rely on this to keep long-lived notes indefinitely until they
> explicitly delete them.

Any change to `purge_old` must preserve this guarantee.

# notes

A tiny notes CLI with soft-delete and a retention cleanup job.

```
python -m notes.cli purge --db notes.json --retention-days 30
```

See `docs/RETENTION_POLICY.md` for the rules the cleanup job must follow,
and run `pytest` to check the test suite.

# Cloud Ingestion Pipeline

An incremental Python ingestion pipeline for **synthetic** JSON telemetry. Start locally; add Docker, CI and AWS S3 after understanding the basics.

## Run

```bash
python3 ingest.py samples/events.jsonl
python3 -m unittest discover -s tests -v
```

Reads JSON Lines, validates required fields, and summarizes accepted/rejected events. No cloud account or credentials required.

## Next exercises

1. Write accepted and rejected events to separate files.
2. Add a CLI output directory.
3. Add Docker and GitHub Actions.
4. Later, replace local input with S3 objects using least-privilege IAM.

**Status:** Local educational starter; AWS integration is not implemented yet.

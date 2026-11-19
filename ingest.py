"""Minimal local JSONL ingestion with no external dependencies."""
import argparse
import json
from pathlib import Path

REQUIRED = ("device_id", "severity", "message")
SEVERITIES = {"DEBUG", "INFO", "WARN", "ERROR"}


def is_valid_event(event: object) -> bool:
    return (
        isinstance(event, dict)
        and all(isinstance(event.get(key), str) and event[key].strip() for key in REQUIRED)
        and event["severity"] in SEVERITIES
    )


def ingest(path: Path) -> dict[str, int]:
    result = {"accepted": 0, "rejected": 0}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            event = None
        result["accepted" if is_valid_event(event) else "rejected"] += 1
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest synthetic JSONL events")
    parser.add_argument("path", type=Path)
    print(json.dumps(ingest(parser.parse_args().path), indent=2))

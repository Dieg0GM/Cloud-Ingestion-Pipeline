FROM python:3.11-slim
WORKDIR /app
COPY ingest.py .
COPY samples/ ./samples/
CMD ["python", "ingest.py", "samples/events.jsonl"]

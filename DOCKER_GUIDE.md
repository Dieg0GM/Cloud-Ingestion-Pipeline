# Docker quickstart

This is an educational container. Docker must be available locally or inside your Codespace.

```bash
docker build -t cloud-ingestion-pipeline .
docker run --rm cloud-ingestion-pipeline
```

Run tests first with `python3 -m unittest discover -s tests -v`. The CI workflow builds this image automatically after tests pass. Do not put secrets into images.

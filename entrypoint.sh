#!/bin/bash
if [ "$PRODUCTION" = "true" ]; then
    exec python3 -m uvicorn main:app --workers $WORKERS --host 0.0.0.0 --port 8000
else
    exec python3 -m debugpy --listen 0.0.0.0:5678 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
fi

#!/bin/bash
if [ "$PRODUCTION" = "true" ]; then
    exec python3 -m uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
else
    exec python3 -m debugpy --listen 0.0.0.0:5678 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
fi

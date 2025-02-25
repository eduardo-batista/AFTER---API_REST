#!/bin/bash
if [ "$PRODUCTION" = "true" ] || [ "$DEBUG" = "false" ]; then
    exec python -m uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
else
    exec python -m debugpy --listen 0.0.0.0:5678 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
fi
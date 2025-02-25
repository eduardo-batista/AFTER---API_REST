"""
main.py

This module contains the main logic of the application.
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.src.controller.example_controller import example_router

app = FastAPI()

app.include_router(example_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint principal que retorna uma mensagem de status."""
    return {"It works!"}

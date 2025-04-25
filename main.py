"""
main.py

This module contains the main logic of the application.
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.src.controller.user_controller import user_router
from api.src.controller.space_controller import space_router

app = FastAPI(
    openapi_tags=[
        {"name": "space", "description": "Gerenciamento de espaços."},
        {"name": "user", "description": "Gerenciamento de Usuários."}
    ]
)

app.include_router(user_router)
app.include_router(space_router)

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

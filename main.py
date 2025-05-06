"""
main.py

This module contains the main logic of the application.
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.src.controller.user_controller import user_router
from api.src.controller.space_controller import space_router
from api.src.controller.tag_controller import tag_router
from api.src.controller.event_controller import event_router

app = FastAPI(
    openapi_tags=[
        {"name": "event", "description": "Gerenciamento de eventos."},
        {"name": "space", "description": "Gerenciamento de espaços."},
        {"name": "tag", "description": "Gerenciamento de tags."},
        {"name": "user", "description": "Gerenciamento de Usuários."}
    ]
)

app.include_router(user_router)
app.include_router(space_router)
app.include_router(tag_router)
app.include_router(event_router)

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

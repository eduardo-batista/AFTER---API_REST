from fastapi import HTTPException
from supabase import create_client, Client
from typing import Optional
import os

from api.src.interface.auth_provider import AuthProvider

class SupabaseAuth(AuthProvider):
    def __init__(self):
        try:
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
            if not url or not key:
                raise ValueError("SUPABASE_URL ou SUPABASE_SERVICE_ROLE_KEY não encontrados.")
            self.client: Client = create_client(url, key)
        except Exception as e:
            raise HTTPException(500, "Erro interno ao conectar ao Supabase.")

    def sign_up(self, email: str, password: str) -> str:
        """Create a Supabase user and return its ID (UUID)"""
        try:
            result = self.client.auth.sign_up({
                "email": email,
                "password": password,
            })
            if result.user:
                return result.user.id
            raise HTTPException(500, "Não foi possível criar o usuário no Supabase.")
        except Exception as e:
            raise HTTPException(400, f"{str(e)}")

    def sign_in(self, email: str, password: str) -> Optional[str]:
        """Sign in to Supabase and return the access token"""
        try:
            result = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password,
            })
            if result.session:
                return result.session.access_token
            raise HTTPException(500, f"Erro ao realizar login no Supabase.")
        except Exception as e:
            raise HTTPException(401, f"{str(e)}")

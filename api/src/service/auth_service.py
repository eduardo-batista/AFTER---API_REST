from api.infra.auth.supabase_auth import SupabaseAuth
from api.src.interface.auth_provider import AuthProvider

class AuthService:
    def __init__(self, provider: AuthProvider = SupabaseAuth()):
        self.provider = provider

    async def register_user(self, email: str, password: str) -> str:
        return self.provider.sign_up(email, password)

    async def login_user(self, email: str, password: str) -> str:
        return self.provider.sign_in(email, password)
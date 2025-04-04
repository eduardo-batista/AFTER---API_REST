import jwt
import bcrypt
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

class Auth:
    @staticmethod
    def hash_password(password: str | None) -> str | None:
        if password:
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        return None

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    @staticmethod
    def create_access_token(user_id: int):
        payload = {
            "sub": user_id,
            "exp": datetime.now()
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload.get("sub")
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

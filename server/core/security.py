from datetime import datetime, timedelta
from fastapi.security import HTTPBearer
import jwt as jwt
from passlib.context import CryptContext


ALGORITHM = "HS256"
SECRET_KEY = 'SECRET'

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def encode_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

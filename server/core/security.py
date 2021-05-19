from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
import jwt


class AuthDetails(BaseModel):
    username: str
    password: str


ALGORITHM = 'HS256'
SECRET_KEY = 'SECRET'

security = HTTPBearer()
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
        algorithm='HS256'
    )


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail='Invalid token')


def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(security)):
    return decode_token(auth.credentials)

import jwt
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
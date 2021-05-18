from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_PREFIX: str = '/api/v1'
    PROJECT_NAME: str = 'FAST API'
    STATIC_AVATAR:str = '/static/avatars/'


settings = Settings()

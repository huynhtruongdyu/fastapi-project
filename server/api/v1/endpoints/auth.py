from fastapi import APIRouter, Depends
from server.core.security import (
    AuthDetails,
    encode_token,
    verify_password
)
from server.schemas import http_response_model
import server.crud.crud_user as userRepo

# from fastapi.security import OAuth2PasswordBearer

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




router = APIRouter()


# @router.post('/register', status_code=201):
# def register()

@router.post('/login')
async def login(auth_details: AuthDetails):
    user = None
    users = await userRepo.get_all()
    for x in users:
        if x['username']==auth_details.username:
            user = x
            break
    
    if (user is None) or (not verify_password(auth_details.password, user['password'])):
        return http_response_model.ErrorResponseModel(None, http_response_model.HttpStatusCode.UNAUTHORIZED, "Invalid username or password")
    token = encode_token(user['username'])
    return {
        'token': token
    }
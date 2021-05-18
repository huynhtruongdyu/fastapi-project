from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.core.security import get_password_hash
from server.crud.crud_user import (
    get_all,
    get_by_id,
    create,
    update,
    delete
)
from server.schemas.http_response_model import *
from server.schemas.user import (
    UserCreateReqModel,
    UserUpdateReqModel
)

# from server.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()


@router.get('/')
async def get_users():
    data = await get_all()
    if data:
        return ResponseModel(data)
    return ErrorResponseModel('no content', HttpStatusCode.NO_CONTENT)


@router.get('/{id}')
async def get_user_by_id(id):
    try:
        data = await get_by_id(id)
        print(data)
        if data:
            return ResponseModel(data)
        return ResponseModel(None, f'Id [{id}] not found')
    except Exception as e:
        return ErrorResponseModel(e, HttpStatusCode.NOT_FOUND)


@router.post('/')
async def create_user(model: UserCreateReqModel = Body(...)) -> dict:
    hashed_pass = get_password_hash(model.password)
    print(hashed_pass)
    model.password = hashed_pass
    user = jsonable_encoder(model)
    print(user)
    new_user = await create(user)
    if new_user:
        return new_user


@router.put('/{id}')
async def update_user(id: str, model: UserUpdateReqModel = Body(...)):
    req = {k: v for k, v in model.dict().items() if v is not None}
    user = await update(id, req)
    if user:
        return ResponseModel([], 'updated')
    return ErrorResponseModel('error.while.update.user', HttpStatusCode.OK)


@router.delete('/{id}')
async def delete_user(id: str):
    user = await delete(id)
    if user:
        return ResponseModel([], 'deleted')
    return ErrorResponseModel('error.while.deleted.user', HttpStatusCode.OK)

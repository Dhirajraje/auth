from fastapi import APIRouter, Depends,status
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.user.model import User
from app.core.db.database import get_session
from app.core.exceptions.api_exceptions import APIException


user_router = APIRouter(tags=['User APIs'])




@user_router.get('/{user_id}')
async def get_user_by_id(user_id,db: AsyncSession = Depends(get_session)):
    try:
        # db.get_on)
        user = {}
        return user
    except Exception as _:
        return APIException()
    



@user_router.get('/')
async def get_users():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    


@user_router.post('/')
async def add_user():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()


@user_router.put('/')
async def put_user():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    
@user_router.patch('/{user_id}')
async def patch_user(user_id):
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    


@user_router.delete('/{user_id}')
async def delete_user(user_id):
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    
  
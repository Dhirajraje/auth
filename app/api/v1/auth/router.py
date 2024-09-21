from fastapi import APIRouter
from app.core.exceptions.api_exceptions import APIException


auth_router = APIRouter(tags=['Authentication APIs'])

@auth_router.post('/sign-up-by-email')
async def sign_up_by_email():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()

@auth_router.post('/sign-in-by-phone')
async def sign_up_by_email():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    


@auth_router.post('/invite-by-email')
async def invite_by_email():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    
@auth_router.post('/sign-in')
async def sign_up_by_email():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    

@auth_router.get('/user')
async def get_current_user():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()


@auth_router.get('/logout')
async def get_current_user():
    try:
        user = {}
        return user
    except Exception as _:
        raise APIException()
    


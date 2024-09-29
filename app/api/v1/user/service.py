from .model import User
from fastcrud import FastCRUD



_user_crud = FastCRUD(User)




async def get_user(db,offset=0,limit=18):
    users =  await _user_crud.get_multi(db,offset=offset,limit=limit)
    print(users)
    return users

async def create_user(db,user):
    _user = await _user_crud.create(db,user)
    return _user

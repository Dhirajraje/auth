from pydantic import BaseModel, Field



class CreateUserSchema(BaseModel):
    username:str
    email:str
    phone:str
    password:str
    

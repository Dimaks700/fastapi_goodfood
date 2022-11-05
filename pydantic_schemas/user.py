from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    name: str
    fullname: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

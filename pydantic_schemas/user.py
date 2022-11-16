from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name: str
    fullname: str

class User(BaseModel):
    username: str
    email: str 
    full_name: str
    password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Login(BaseModel):
    email: str
    password: str
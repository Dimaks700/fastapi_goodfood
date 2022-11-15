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
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

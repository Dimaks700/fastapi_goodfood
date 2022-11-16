from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import api.utils.users as utils
from db.database import async_get_db, get_db
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic_schemas.user import Token, TokenData, User, UserInDB, UserBase

users_router = APIRouter()

@users_router.post("")
async def create_user(user: User, db: Session = Depends(get_db)):
    result = utils.create_user(user=user, db=db)
    return result.id

@users_router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = utils.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.email, db_user.fullname, db_user.name

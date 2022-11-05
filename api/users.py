from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.users import create_user, get_user, get_user_by_email
from db.database import async_get_db, get_db
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic_schemas.user import User, UserCreate

users_router = APIRouter()
    
@users_router.post("/", response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)

@users_router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
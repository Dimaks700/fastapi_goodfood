from sqlalchemy.orm import Session
from db.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic_schemas.user import UserCreate
from sqlalchemy import text

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    #
    user = db.execute(text(
        "SELECT  id, name, fullname, email, encode(user_account.hashed_password, 'escape') FROM user_account"
        ))
    return user
    #return db.query(User).filter(User.name == username).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, name=user.name, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

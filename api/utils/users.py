from sqlalchemy.orm import Session
from db.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic_schemas import user
from sqlalchemy import text
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: user.User):
    db_user = User(
        name=user.username, fullname=user.full_name, email=user.email, 
        hashed_password=get_password_hash(user.password)
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
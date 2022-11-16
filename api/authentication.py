from fastapi import APIRouter, Depends, HTTPException, status
from pydantic_schemas.user import Login
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from db.models import User
from sqlalchemy.orm import Session
import api.utils.users as utils
from sqlalchemy import text
from .token import create_access_token

router = APIRouter()

@router.post("")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect email")
    else:
        if not utils.verify_password(request.password, str(user.hashed_password)):
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
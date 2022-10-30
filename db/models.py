from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(30), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    resipes = relationship("Recipe", back_populates="author")

class Recipe(Base):
    __tablename__ = "user_recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    
    author = relationship("User", back_populates="resipes")
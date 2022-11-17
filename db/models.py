from sqlalchemy import Column, ForeignKey, Integer, String, Text, Table
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(30), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    resipes = relationship("Recipe", back_populates="author")

recipe_ingredients = Table(
    "recipe_ingredients", Base.metadata,
    Column("recipe_id", ForeignKey("user_recipes.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
)

class Recipe(Base): 
    __tablename__ = "user_recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    
    author = relationship("User", back_populates="resipes")
    ingredients = relationship("Ingredient", secondary="recipe_ingredients", back_populates="resipes")

class Ingredient(Base): 
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)

    resipes = relationship("Recipe", secondary="recipe_ingredients", back_populates="ingredients")
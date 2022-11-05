from sqlalchemy.orm import Session

from db.models import Recipe
from pydantic_schemas.recipe import RecipeCreate

async def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def get_recipes(db: Session):
    return db.query(Recipe).all()

def get_user_recipes(db: Session, user_id: int):
    recipe = db.query(Recipe).filter(Recipe.user_id == user_id).all()
    return recipe

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        user_id=recipe.user_id,
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

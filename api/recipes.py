from api.utils.recipes import create_recipe, get_recipes
from db.database import get_db
from db.models import Recipe
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic_schemas.recipe import RecipeCreate
from pydantic_schemas.user import User
from sqlalchemy.orm import Session
from api.oauth2 import get_current_user

recipes_router = APIRouter()

templates = Jinja2Templates(directory="templates") 

@recipes_router.get("/", response_class=HTMLResponse)
async def hello(
    request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
    ):
    recipes = get_recipes(db=db)
    response = {"request": request, "recipes": recipes}
    return templates.TemplateResponse(
        "hello.html", response
    )

@recipes_router.post("/recipes", response_model=RecipeCreate)
async def create_new_recipe(
    recipe: RecipeCreate, db: Session = Depends(get_db)
):
    return create_recipe(db=db, recipe=recipe)

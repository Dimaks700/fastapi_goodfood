from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.recipes import create_recipe, get_recipes
from db.database import get_db
from db.models import Recipe
from pydantic_schemas.recipe import RecipeCreate

recipes_router = APIRouter()

templates = Jinja2Templates(directory="templates") 

@recipes_router.get("/", response_class=HTMLResponse)
async def hello(request: Request, db: Session = Depends(get_db)):
    recipes = get_recipes(db=db)
    return templates.TemplateResponse(
        "hello.html", {"request": request, "id": id, "recipes": recipes}
    )

@recipes_router.post("/recipes", response_model=RecipeCreate)
async def create_new_recipe(
    recipe: RecipeCreate, db: Session = Depends(get_db)
):
    return create_recipe(db=db, recipe=recipe)

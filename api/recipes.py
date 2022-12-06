import os
from api.utils.recipes import create_ingredients_pdf, create_recipe, get_recipe, get_recipes, get_resipes_by_ingredient
from db.database import get_db
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic_schemas.recipe import RecipeCreate, Ingredients
from pydantic_schemas.user import User
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks

from api.oauth2 import get_current_user

recipes_router = APIRouter()

templates = Jinja2Templates(directory="templates") 

@recipes_router.get("/", response_class=HTMLResponse)
async def hello(request: Request, db: Session = Depends(get_db)):
    recipes = get_recipes(db=db)
    response = {"request": request, "recipes": recipes}
    return templates.TemplateResponse(
        "hello.html", response
    )

@recipes_router.post("/recipes", response_model=RecipeCreate)
async def create_new_recipe(
    recipe: RecipeCreate, ingrediens: Ingredients, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return create_recipe(db=db, recipe=recipe, ingrediens=ingrediens)

@recipes_router.get("/{recipe_id}")
async def read_recipe(recipe_id, request: Request, db: Session = Depends(get_db)):
    recipe = get_recipe(db=db, recipe_id=recipe_id)
    context  = {"request": request, "recipe": recipe}
    return templates.TemplateResponse(
        "recipe_detail.html", context
    )

@recipes_router.get("/{recipe_id}/download")
async def download_ingredients(
    recipe_id, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
    ):
    background_tasks.add_task(os.unlink, f"static/{recipe_id}.pdf")
    return FileResponse(create_ingredients_pdf(db, recipe_id))

@recipes_router.get("/ingredient/recipes_by")
async def recipes_by_ingredient(ingredient: str, db: Session = Depends(get_db)):
    return get_resipes_by_ingredient(db=db, ingredient=ingredient)
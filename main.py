import imp
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import users, recipes
from db.database import engine
#from db.models import User, Recipe
from db import models

models.Base.metadata.create_all(bind=engine)

#User.Base.metadata.create_all(bind=engine)
#Recipe.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI GoodFood",
    description="Сайт с классными рецептами", 
    contact={
        "name": "Dmitry",
        "email": "vanomas09@gmail.com",
    },
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(recipes.recipes_router, prefix="")
app.include_router(users.users_router, prefix="/users")
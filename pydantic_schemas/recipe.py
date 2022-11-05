from pydantic import BaseModel

class RecipeBase(BaseModel):
    title : str
    user_id: int
    class Config:
        orm_mode = True

class RecipeCreate(RecipeBase):
    description : str

class Recipe(RecipeBase):
    id: int

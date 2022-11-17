from sqlalchemy.orm import Session
from fpdf import FPDF
from db.models import Recipe
from pydantic_schemas.recipe import RecipeCreate

def get_recipe(db: Session, recipe_id: int):
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

def create_ingredients_pdf(db: Session, recipe_id: int):
    path = f'static/{recipe_id}.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    recipe = get_recipe(db=db, recipe_id=recipe_id)
    name = recipe.title
    pdf.cell(50, 15, "GoodFood", 1, 0, 'C')
    pdf.ln(20)
    enumerated_list = list(enumerate([i.title for i in recipe.ingredients], 1))
    enumerated_str = [f"{str(i[0])}. {i[1]}" for i in enumerated_list]
    for i in enumerated_str:
        pdf.cell(w=40, h=10, txt=i, ln=10)
    pdf.output(path, 'F')
    return path

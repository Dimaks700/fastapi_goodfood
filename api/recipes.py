from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

recipes_router = APIRouter()

templates = Jinja2Templates(directory="templates") 

@recipes_router.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request, "id": id})

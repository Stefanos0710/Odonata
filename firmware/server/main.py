from os import path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

if path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
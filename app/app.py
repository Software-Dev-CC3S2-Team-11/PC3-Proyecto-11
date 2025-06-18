"""
URL-SHORTENER V0
"""

import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from routes.auth import router as auth_router
from services.auth import verify_token
from dotenv import load_dotenv
from os import getenv
from core.settings import HOST, PORT
from routes.url import router as url_router
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.requests import Request

load_dotenv()

SESSION_SECRET = getenv('SESSION_SECRET')

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)
app.include_router(auth_router)
# Renderiza los html usando Jinja2
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")


@app.get('/register', response_class=HTMLResponse)
async def register(request: Request):
    """
    Renderiza la página de registro
    """
    token = request.session.get("token")
    if token:
        payload = verify_token(token)
        if payload:
            return RedirectResponse(url="/")

    return templates.TemplateResponse('register.html', {
        "request": request, "page": "register"
    })


@app.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    """
    Renderiza la página de inicio de sesión
    """
    token = request.session.get("token")
    if token:
        payload = verify_token(token)
        if payload:
            return RedirectResponse(url="/")

    return templates.TemplateResponse('login.html', {
        "request": request, "page": "login"
    })


@app.get('/dashboard', response_class=HTMLResponse)
async def dashboard(request: Request):
    """
    Renderiza la página de dashboard
    """
    token = request.session.get("token")

    if not token:
        return RedirectResponse(url="/")

    payload = verify_token(token)

    if not payload:
        return RedirectResponse(url="/")

    username = payload.get("username")

    return templates.TemplateResponse('dash.html', {
        "request": request,
        "username": username
    })

app.include_router(url_router)

if __name__ == "__main__":
    print('V0')
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import UsuarioModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Página de inicio (login visual)
@router.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "titulo": "Login | Finantel Group"})

# Procesar login
@router.post("/", response_class=HTMLResponse)
def procesar_login(request: Request, email: str = Form(...), password: str = Form(...)):
    usuario = UsuarioModel.autenticar(email, password)

    if usuario:
        print(f"✅ Usuario autenticado: {usuario['email']}")
        return RedirectResponse(url="/home", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "titulo": "Login | Finantel Group",
            "error": "Email o contraseña incorrectos"
        })

# Página de home
@router.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "titulo": "Home | Finantel Group"})

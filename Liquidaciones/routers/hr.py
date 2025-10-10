from fastapi import APIRouter, HTTPException
from dto.usuario import UsuarioCreate, UsuarioLogin
from models.usuario_model import UsuarioModel

router = APIRouter(prefix="/hr", tags=["Recursos Humanos"])

@router.post("/registro")
def registrar_usuario(usuario: UsuarioCreate):
    try:
        UsuarioModel.registrar(usuario)
        return {"mensaje": "Usuario registrado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login_usuario(usuario: UsuarioLogin):
    if UsuarioModel.verificar(usuario.username, usuario.password):
        return {"mensaje": "Login exitoso", "usuario": usuario.username}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
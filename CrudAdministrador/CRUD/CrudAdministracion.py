# backend.py

USUARIOS = {
    "ninja": "1234",
    "sasuke": "uchiha",
    "naruto": "hokage"
}

def verificar_usuario(usuario, contrasena):
    return USUARIOS.get(usuario) == contrasena

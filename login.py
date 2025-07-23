from CrudAdministrador.CRUD import CrudAdministracion as administracion
import os
ruta = "Archivos/usuario.txt"

def abrirArchivo():
    if not os.path.exists(ruta):
        open(ruta, 'w').close()

def registrarUsuario(): 
    numeros = "1234567890"
    n_numeros = False
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    n_mayusculas = False
    print("Registrando Usuario")
    nombre = input("Nombre: ")
    apellido = input("Apelldo: ")
    nombres = f"{nombre} {apellido}" 
    edad = input("Edad: ")
    usuario = f"{nombre.lower()}.{apellido.lower()}@gmail.com" 
    print()
    with open(ruta,"r") as archivo: 
        for l in archivo:                     
            if usuario in l:
                print("El usuario ya existe!!")
                return
    print(f"Su usuario es: {usuario}")
    while True:
        print("La contraseña debe tener minimo 8 caracteres, 1 numero, 1 mayuscula")
        contraseña = input("Contraseña: ")
        if len(contraseña)<8:
            print("Contraseña corta")
        else:
            for i in range(len(mayusculas)):
                if mayusculas[i] in contraseña:
                    n_mayusculas = True
            for i in range(len(numeros)):
                if numeros[i] in contraseña:
                    n_numeros = True
            if n_mayusculas and n_numeros:
                print("Contraseña valida")
                break
    esAdmin=input("Es admin? (si/no): ")
    if esAdmin.lower() == "si":
        admin = 1
    elif esAdmin.lower() == "no":
        admin = 0
    else:
        print("Escriba una opcion valida")
    with open(ruta,"a") as usuarios:
        usuarios.write(f"{usuario}|{contraseña}|{nombres}|{edad}|{admin}\n")

def iniciarSesion():
    intento = 0
    usuario_correcto="admin" 
    contraseña_correcta="admin"
    print("Inicio de Sesion")
    while intento<3:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        with open(ruta,"r") as usuarios:
            for l in usuarios: 
                if usuario in l: 
                    usuario_correcto=l.split('|')[0]
                    contraseña_correcta=l.split('|')[1]
                    admin = int(l.split('|')[-1])
        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Bienvenido")
            if admin == 1:
                administracion.menuAdministrador()
                break
            else:
                pass#<- temporal, hace que no mande error por no tener nada
                #menuUsuario()
            exit()
        else:
            print("Error") 
            print()
            intento += 1
    print()
    print("Regresando")

def ingresar(): 
    abrirArchivo()
    while True:    
        print("\n1. Iniciar Sesion") 
        print("2. Registrar Cuenta")
        print("3. Cerrar")
        opcion= input("Que quiere hacer?: ")
        if opcion == '1':
            iniciarSesion()
        elif opcion == '2':
            registrarUsuario()
        elif opcion == '3':
            print("Cerrando") 
            break
        else:
            print("Escriba una opcion valida")

import estructuras
import archivos
import funcionesAdministrador
import funcionesUsuario

def obtener_email_usuario(email):
    return email

def listarNinjas():
    if not estructuras.diccionarioNinjas:
        print("No hay ninjas registrados.")
        return

    print("\n--- Lista de Ninjas ---")
    for ninja in estructuras.diccionarioNinjas.items():
        print(f"Ninja: {ninja[0]} Estilo: {ninja[1]['Estilo']}")

#FUNCION MENU ADMINISTRADOR
def menuAdministrador():
    while True:
        print("1. Listar Personajes")
        print("2. Agregar Ninjas")
        print("3. Consultar Ninja")
        print("4. Actualizar Ninja")
        print("5. Eliminar Ninja")
        print("6. Crear Habilidades de Ninja")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case '1':
                listarNinjas()
            case '2':
                funcionesAdministrador.agregarNinja()
            case '3':
                funcionesAdministrador.consultarNinja(funcionesAdministrador.buscarNinja())
            case '4':
                funcionesAdministrador.actualizarNinja(funcionesAdministrador.buscarNinja())
            case '5':
                funcionesAdministrador.eliminarNinja(funcionesAdministrador.buscarNinja())
            case '6':
                funcionesAdministrador.crearHabilidadNinja()
                archivos.guardarHabilidades()
            case '7':
                print("Saliendo")
                break
            case _:
                print("Escriba una opcion valida")

#FUNCION MENU USUARIO
def menuUsuario(usuario_email):
    while True:
        print("1. Listar Personajes")
        print("2. Pelear contra ninjas")
        print("3. Comenzar Torneo")
        print("4. Ver Ranking")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case '1':
                listarNinjas()
            case '2':
                funcionesUsuario.pvp(usuario_email)
            case '3':
                funcionesUsuario.torneoNinja()
            case '4':
                funcionesUsuario.mostrar_ranking()
            case '5':
                print("Saliendo")
                break
            case _:
                print("Escriba una opcion valida")

#FUNCIONES LOGIN

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
    with open("usuarios.txt","r") as archivo: 
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
    with open("usuarios.txt","a") as usuarios:
        usuarios.write(f"{usuario}|{contraseña}|{nombres}|{edad}|{admin}\n")

def iniciarSesion():
    intento = 0
    usuario_correcto="admin" 
    contraseña_correcta="admin"
    admin = 1
    print("Inicio de Sesion")
    while intento<3:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        with open("usuarios.txt","r") as usuarios:
            for l in usuarios: 
                if usuario in l: 
                    usuario_correcto=l.split('|')[0]
                    contraseña_correcta=l.split('|')[1]
                    admin = int(l.split('|')[-1])
        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Bienvenido")
            obtener_email_usuario(usuario_correcto)
            if admin == 1:
                menuAdministrador()
                break
            else:
                menuUsuario(usuario)
                break
        else:
            print("Error") 
            print()
            intento += 1
    print()
    print("Regresando")

def ingresar(): 
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
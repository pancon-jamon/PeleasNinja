import estructuras
import funcionesAdministrador
import funcionesUsuario

def listarNinjas():
    if not estructuras.diccionarioNinjas:
        print("No hay ninjas registrados.")
        return

    print("\n¿Ordenar por?")
    print("1. Nombre (A-Z)")
    print("2. Puntos (mayor a menor)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ninjas_ordenados = sorted(estructuras.diccionarioNinjas.items())
    elif opcion == "2":
        ninjas_ordenados = sorted(estructuras.diccionarioNinjas.items(), key=lambda x: x[1][4], reverse=True)
    else:
        print("Opción inválida.")
        return

    print("\n--- Lista de Ninjas ---")
    for nombre, atributos in ninjas_ordenados:
        print(f"""
            Nombre: {nombre}
            Fuerza: {atributos[0]}
            Agilidad: {atributos[1]}
            Resistencia: {atributos[2]}
            Estilo de pelea: {atributos[3]}
            Puntos: {atributos[4]}
            """)

#FUNCION MENU ADMINISTRADOR
def menuAdministrador():
    while True:
        print("1. Listar Personajes")
        print("2. Agregar Ninjas")
        print("3. Consultar Ninja")
        print("4. Actualizar Ninja")
        print("5. Eliminar Ninja")
        print("6. Crear Habilidades de Ninja")
        print("7. Guardar Cambios")
        print("8. Salir")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case '1':
                listarNinjas()
            case '2':
                funcionesAdministrador.agregarNinja()
            case '3':
                funcionesAdministrador.consultarNinja(funcionesAdministrador.buscarNinja())
            case '4':
                pass#Funcion No lista
            case '5':
                funcionesAdministrador.eliminarNinja(funcionesAdministrador.buscarNinja())
            case '6':
                pass#Funcion No lista
            case '7':
                pass#Funcion No lista
            case '8':
                print("Saliendo")
                break
            case _:
                print("Escriba una opcion valida")

#FUNCION MENU USUARIO
def menuUsuario():
    while True:
        print("1. Listar Personajes")
        print("2. Pelear contra ninjas")
        print("3. Comenzar Torneo")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case '1':
                listarNinjas()
            case '2':
                pass#Funcion No lista
            case '3':
                pass#Funcion No lista
            case '4':
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
            if admin == 1:
                menuAdministrador()
                break
            else:
                menuUsuario()
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
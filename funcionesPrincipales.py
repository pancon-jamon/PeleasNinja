import estructuras
import funcionesAdministrador
import funcionesUsuario
import os

archivo_usuarios = "Archivos/usuarios.txt"

def obtener_email_usuario(email):
    return email

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

        try:
            opcion = int(input("Seleccione una opción: "))

            if not opcion:
                print("No puede dejar el campo vacío!")
                continue
            if not 1 <= opcion <= 3:
                print("Opción inválida, por favor intente de nuevo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        match opcion:
            case 1:
                listarNinjas()
            case 2:
                funcionesAdministrador.agregarNinja()
            case 3:
                funcionesAdministrador.consultarNinja(funcionesAdministrador.buscarNinja())
            case 4:
                funcionesAdministrador.actualizarNinja()
            case 5:
                funcionesAdministrador.eliminarNinja(funcionesAdministrador.buscarNinja())
            case 6:
                funcionesAdministrador.crearHabilidadesNinja()
            case 7:
                funcionesAdministrador.guardarCambios()
            case 8:
                print("Saliendo...")
                break
            case _:
                print("Escriba una opcion valida")

#FUNCION MENU USUARIO
def menuUsuario(usuario_email):
    while True:
        print("\n1. Listar Personajes")
        print("2. PvP")
        print("3. Torneo")
        print("4. Ver Ranking")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))

            if not opcion:
                print("No puede dejar el campo vacío!")
                continue
            if not 1 <= opcion <= 5:
                print("Opción inválida, por favor intente de nuevo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        match opcion:
            case 1:
                listarNinjas()
            case 2:
                funcionesUsuario.pvp(usuario_email)
            case 3:
                funcionesUsuario.torneoNinja()
            case 4:
                funcionesUsuario.mostrar_ranking()
            case 5:
                break
            case _:
                print("Opción inválida")

#FUNCIONES LOGIN

def registrarUsuario(): 
    numeros = "1234567890"
    n_numeros = False
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    n_mayusculas = False

    print("Registrando Usuario")

    while True:
        nombre = input("Nombre: ")
        if not nombre.strip():
            print("El nombre no puede estar vacío.")
            continue

        apellido = input("Apelldo: ")
        if not apellido.strip():
            print("El apellido no puede estar vacío.")
            continue
        break

    nombres = f"{nombre} {apellido}" 

    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")

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

    while True:
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
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    with open("usuarios.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split("|")
            if usuario == datos[0] and contraseña == datos[1]:
                obtener_email_usuario(datos[0])
                if datos[2] == "1":
                    menuAdministrador()
                else:
                    menuUsuario(usuario)
                return
    print("Login incorrecto.")

def ingresar(): 
    while True:    
        print("\n1. Iniciar Sesion") 
        print("2. Registrar Cuenta")
        print("3. Cerrar")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if not opcion:
                print("No puede dejar el campo vacio")
                continue
            if not 1 <= opcion <= 3:
                print("Opcion invalida, por favor intente de nuevo.")
                continue

        except ValueError:
            print("Por favor, ingrese un numero.")
            continue
        
        if opcion == 1:
            if not os.path.exists("usuarios.txt"):
                open("usuarios.txt", "w").close()
                print("No hay usuarios registrados. Por favor, registre una cuenta.")
                registrarUsuario()
                print(end="\r")

            iniciarSesion()
        elif opcion == 2:
            registrarUsuario()
        elif opcion == 3:
            print("Cerrando") 
            break
        else:
            print("Escriba una opcion valida")

ingresar()

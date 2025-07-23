#estructuraDiccionarioNinjas ={nombre : [fuerza, agilidad, resistencia, estilo, puntos] }
import os

estructuraDiccionarioNinjas = {}

def encontrarNinja(ninjaConsulta, ninjas):
    """
    Busca un ninja por su nombre en un diccionario de ninjas
    y retorna sus habilidades si es encontrado.

    Args:
        ninjaConsulta (str): Nombre del ninja a buscar. No importa si está en mayúsculas o minúsculas.
        ninjas (dict): Diccionario donde las claves son los nombres de los ninjas (str)
                       y los valores son listas con sus habilidades (list).

    Returns:
        dict: Un diccionario con el nombre del ninja como clave y una lista con sus primeras habilidades
              como valor, si se encuentra.
              Si no se encuentra, retorna un diccionario vacío y muestra un mensaje en pantalla.

    Example:
        ninjas = {
            "Naruto": ["Rasengan", "Sombra", "Kurama", "Modo sabio", "Clones", "Modo Baryon"],
            "Sasuke": ["Sharingan", "Rinnegan", "Chidori", "Amaterasu", "Susanoo"]
        }

        encontrarNinja("naruto", ninjas)
        # Output: {'Naruto': ['Rasengan', 'Sombra', 'Kurama', 'Modo sabio', 'Clones']}
    """
    for nombreNinja, habilidadesNinja in ninjas.items():
        if ninjaConsulta.lower() == nombreNinja.lower():
            return {nombreNinja: habilidadesNinja}
    print('El ninja no está registrado en este sistema.')
    return {}

def actualizarNinja():
    while True:
        nombreActulizar = input('Ingrese el nombre del ninja a actualizar: ').split()
        if not nombreActulizar:
            print('No puede dejar el campo vacio!')
            continue
        if not encontrarNinja(nombreActulizar):
            print('No se encontro coincidencias')
            continue
        else:
            break
    agregarNinja(nombreActulizar)
    print(f"Ninja {nombreActulizar} actualizado con éxito.")

def cargarNinjas():
    if os.path.exists("ninjas.txt"):
        with open("ninjas.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                nombre = datos[0]
                fuerza = int(datos[1])
                agilidad = int(datos[2])
                resistencia = int(datos[3])
                estilo = datos[4]
                puntos = int(datos[5])
                estructuraDiccionarioNinjas[nombre] = [fuerza, agilidad, resistencia, estilo, puntos]

def guardarNinja(nombre, características):
    with open("ninjas.txt", "a") as f:
        f.write(f"{nombre}|{características[0]}|{características[1]}|{características[2]}|{características[3]}|{características[4]}\n")

def agregarNinja(nombre):
    try:
        fuerza = int(input("Fuerza (0-100): "))
        agilidad = int(input("Agilidad (0-100): "))
        resistencia = int(input("Resistencia (0-100): "))
        estilo = input("Estilo de pelea: ").strip()
        puntos = int(input("Puntos iniciales: "))
    except ValueError:
        print("Error ingrese valores válidos.")
        return

    estructuraDiccionarioNinjas[nombre] = [fuerza, agilidad, resistencia, estilo, puntos]
    guardarNinja(nombre, estructuraDiccionarioNinjas[nombre])
    
def agregarNinjaNuevo():
    nombre = input("Nombre del ninja: ").strip()
    if nombre in estructuraDiccionarioNinjas:
        print("Ese ninja ya está registrado.")
        return
    agregarNinja(nombre)
    print(f"Ninja {nombre} agregado con éxito.")

def listarNinjas():
    if not estructuraDiccionarioNinjas:
        print("No hay ninjas registrados.")
        return

    print("\n¿Ordenar por?")
    print("1. Nombre (A-Z)")
    print("2. Puntos (mayor a menor)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ninjas_ordenados = sorted(estructuraDiccionarioNinjas.items())
    elif opcion == "2":
        ninjas_ordenados = sorted(estructuraDiccionarioNinjas.items(), key=lambda x: x[1][4], reverse=True)
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

#consultar y actualizar ninja
def consultarNinja():
    
    while True:
        ninjaConsulta = input('Ingrese el nombre del ninja a consultar: ').strip().lower()

        if not ninjaConsulta:
            print('El campo no puede estar vacío. Inténtelo nuevamente')
            continue  # Solo agregué 'continue' para reiniciar el bucle
        
        ninja_encontrado = False  # Bandera para saber si lo encontramos
        for nombreNinja, habilidadesNinja in ninjas.items():
            if ninjaConsulta == nombreNinja.lower():  # Comparación en minúsculas
                ninja_encontrado = True
                # Asumo que habilidadesNinja es [fuerza, agilidad, resistencia, estilo, puntos]
                return (
                    f'Nombre del ninja: {nombreNinja}\n'
                    f'Fuerza: {habilidadesNinja[0]}\n'
                    f'Agilidad: {habilidadesNinja[1]}\n'
                    f'Resistencia: {habilidadesNinja[2]}\n'
                    f'Estilo: {habilidadesNinja[3]}\n'
                    f'Puntos: {habilidadesNinja[4]}'
                )
        if not ninja_encontrado:  # Solo muestra el error si no se encontró después de buscar todos
            print('El ninja no está registrado en este sistema.')
        
def menuAdministrador(): 
    while True:
        try:
            print("1. Agregar ninjas")
            print("2. Listar ninjas")
            print("3. Consultar ninjs")
            print("4. Actualizar ninja")
            print("5. Eliminar ninja")
            print("6. Crear arbol de habilidades")
            print("7. Guardar cambios")
            print("8. Salir")
            opcion = int(input('Ingrese una opcion: '))

            if not opcion:
                print('No puede dejar el campo vacio')

            if 1<opcion<4:
                print('Ingrese una opcion entre 1-4')
            else:
                break
                
        except ValueError:
            print('Porfavor ingrese una opcion valida')

    if opcion == 1:
        agregarNinja()
    if opcion == 2:
        listarNinjas()
    if opcion == 3:
        consultarNinja()
    if opcion == 4:
        actualizarNinja()
    if opcion == 5:
        pass#debemos esperar a eliminarNinjas
    if opcion == 6:
        pass#debemos esperar a crear arboles
    if opcion == 7:
        guardarNinja()
    if opcion == 8:
        print('Saliendo...')

    

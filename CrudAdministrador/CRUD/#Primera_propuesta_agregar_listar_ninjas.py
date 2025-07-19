#Primer propuesta de codigo de agregar ninjas
#Gabriel Toaquiza
#estructuraDiccionarioNinjas ={nombre : [fuerza, agilidad, resistencia, estilo, puntos] }
import os

estructuraDiccionarioNinjas = {}

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

def agregarNinja():
    nombre = input("Nombre del ninja: ").strip()
    if nombre in estructuraDiccionarioNinjas:
        print("Ese ninja ya está registrado.")
        return

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


cargarNinjas()

agregarNinja()

listarNinjas()
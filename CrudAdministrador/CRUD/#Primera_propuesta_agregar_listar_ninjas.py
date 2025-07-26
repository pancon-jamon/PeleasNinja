#Primer propuesta de codigo de agregar ninjas
#Gabriel Toaquiza
#estructuraDiccionarioNinjas ={nombre : [fuerza, agilidad, resistencia, estilo, puntos] }
import os
import random

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
    #cambio a la funcion agregar
    fuerza = random.randint(5,10)
    agilidad = random.randint(5,10)
    resistencia = random.randint(5,10)
    estilo = input("Estilo de pelea: ").strip()
    puntos = fuerza + agilidad + resistencia
    

    estructuraDiccionarioNinjas[nombre] = [fuerza, agilidad, resistencia, estilo, puntos]
    guardarNinja(nombre, estructuraDiccionarioNinjas[nombre])
    print(f"Ninja {nombre} agregado con éxito.")

def listarNinjas():
    if not estructuraDiccionarioNinjas:
        print("No hay ninjas registrados.")
        return
    
    print(f"El numero de ninjas que hay es de {len(estructuraDiccionarioNinjas)}")
    print("Ordenar por:")
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
        #nueva funcion
def pelea(ninja1,ninja2):
        datos1 = estructuraDiccionarioNinjas[ninja1]
        datos2 = estructuraDiccionarioNinjas[ninja2]
        print(f"{ninja1} VS {ninja2}")
        print(f"{ninja1}\nEstadisticas:\nFuerza: {datos1[0]}\nAgilidad: {datos1[1]}\nResistencia: {datos1[2]}\nEstilo de pelea: {datos1[3]}\nPuntos: {datos1[4]}\n")
        print(f"{ninja2}\nEstadisticas:\nFuerza: {datos2[0]}\nAgilidad: {datos2[1]}\nResistencia: {datos2[2]}\nEstilo de pelea: {datos2[3]}\nPuntos: {datos2[4]}\n")
        if estructuraDiccionarioNinjas[ninja1][4]<estructuraDiccionarioNinjas[ninja2][4]:
            print(f"{ninja2} es el ganador del enfrentamiento\n")
            return ninja2
        else:
            print(f"{ninja1} es el ganador del enfrentamiento\n")
            return ninja1
#nueva funcion
def torneoNinja():
    if len(estructuraDiccionarioNinjas)<16:
        print("No hay suficientes ninjas en la lista")
        return
    pila = []
    ninjas = random.sample(list(estructuraDiccionarioNinjas.keys()),16)
    for ninja in ninjas:
        pila.append(ninja)
    print("Torneo Ninja?")
    print("\n*****Enfrentamientos 16vos*****\n")
    while len(pila) > 8:
        ninja1 = pila.pop()
        ninja2 = pila.pop()
        ganador = pelea(ninja1,ninja2)
        print(f"El ganador es {ganador}")
        pila.append(ganador)
    print("\n*****Enfrentamientos 8vos*****\n")
    while len(pila) > 4:
        ninja1 = pila.pop()
        ninja2 = pila.pop()
        ganador = pelea(ninja1,ninja2)
        print(f"El ganador es {ganador}")
        pila.append(ganador)
    print("\n*****Enfrentamientos semifinales*****\n")
    while len(pila) > 2:
        ninja1 = pila.pop()
        ninja2 = pila.pop()
        ganador = pelea(ninja1,ninja2)
        print(f"El ganador es {ganador}")
        pila.append(ganador)
    print("\n*****Final*****\n")
    if len(pila) == 2:
        ninja1 = pila.pop()
        ninja2 = pila.pop()
        ganador = pelea(ninja1,ninja2)
        print(f"El ganador del torneo es {ganador}")
##Nueva función
def menu():
    cargarNinjas()
    while True:
        print("Menu de seleccion\n1.Agregar ninja\n2.Listar ninjas\n3.Torneo de ninjas\n4.Salir")
        opcion = int(input("Ingrese la opcion que desea: "))
        if opcion ==1:
            agregarNinja()
        elif opcion ==2:
            listarNinjas()
        elif opcion == 3:
            torneoNinja()
        elif opcion == 4:
            break
        else:
            print("Ingrese una opcion válida")

menu()
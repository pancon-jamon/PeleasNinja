import random 
import os
archivo = "habilidades_ninja.txt"
#Árbol general de habilidades ninja
#con posibildidad de organizarse en preorden, inorden y postorden dependiendo de cómo vaya la pelea
#tanque, tirador, asesino

"""
Librearías:
os: se emplea para archivos.
random: en este caso puntual, para asignar aleatoriamente los estilos de pelea (árboles de habilidades)
        a los peleadores.

Funciones: 
crear_archivo_habilidades(): crea y guarda los árboles binarios de habilidades de cada estilo de pelea de los ninjas, 
                             en caso de ya existir el archivo no lo va a crear.
asignarEstiloAleatorio(lista_ninjas,lista_estilos): asigna aleatoriamente los estilos de pelea (árboles de habilidades)
                                                    a cada ninja creado.
"""

estiloTirador_habilidades = {
    "habilidad":"Flecha de Cristal Encantada",
    "puntos":5,
    "izquierda":{"habilidad":"Tiro Místico",
                 "puntos":4,
                 "izquierda":{"habilidad":"Disparo Halcón",
                              "puntos":2,
                              "izquierda":None,"derecha":None                     
                 },
                 "derecha":None
    },
    "derecha":{"habilidad":"Lluvia de Kunais",
               "puntos":3,
               "izquierda":None,"derecha":None
    }
}

estiloAsesino_habilidades = {
    "habilidad":"Último Suspiro",
    "puntos":5,
    "izquierda":{"habilidad":"Ejecución Perfecta",
                 "puntos":4,
                 "izquierda":None,"derecha":None
    },
    "derecha":{"habilidad":"Guillotina",
               "puntos":3,
               "izquierda":{"habilidad":"Golpe Rápido",
                            "puntos":2,
                            "izquierda":None,"derecha":None                   
               },
               "derecha":None
    }
}

estiloTanque_habilidades = {
    "habilidad":"Heraldo de la Destrucción",
    "puntos":5,
    "izquierda":{"habilidad":"Golpe Decisivo",
                 "puntos":4,
                 "izquierda":None,
                 "derecha":{"habilidad":"Golpe Meteoro",
                            "puntos":2,
                            "izquierda":None,"derecha":None                     
                 }
    },
    "derecha":{"habilidad":"Grito Primal",
               "puntos":3,
               "izquierda":None,"derecha":None
    }
}

def crearArchivoHabilidades():
    if not os.path.exists(archivo):
        with open(archivo, "w", encoding="utf-8") as file:
            file.write("Estilo de pelea Tirador:\n")
            file.write(str(estiloTirador_habilidades))
            file.write("\nEstilo de pelea Asesino:\n")
            file.write(str(estiloAsesino_habilidades))
            file.write("\nEstilo de pelea Tanque:\n")
            file.write(str(estiloTanque_habilidades))

crearArchivoHabilidades()

ninjas = ["Naruto","Sasuke","Sakura"]
estilos = {"Tirador":estiloTirador_habilidades,"Asesino":estiloAsesino_habilidades,"Tanque":estiloTanque_habilidades}

def asignarEstiloAleatorio(lista_ninjas,lista_estilos):
    habilidades_asignadas = {}
    for ninja in lista_ninjas:
        estilo, arbol = random.choice(list(lista_estilos.items()))
        habilidades_asignadas[ninja] = {"estilo":estilo,"arbol":arbol}
    return habilidades_asignadas

asignarEstiloAleatorio(ninjas, estilos)

asignacion = asignarEstiloAleatorio(ninjas, estilos)
for nombre, datos in asignacion.items():
    estilo = datos["estilo"]
    print(f"Nombre: {nombre}; Estilo: {estilo}")

#para elegir los tipos de ataques
def inorden(nodo): #ofensivo
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades += inorden(nodo["izquierda"])
        recorrido_habilidades.append(nodo["habilidad"])
        recorrido_habilidades += inorden(nodo["derecha"])
    return recorrido_habilidades

def preorden(nodo): #equilibrado
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades.append(nodo["habilidad"])
        recorrido_habilidades += preorden(nodo["izquierda"])
        recorrido_habilidades += preorden(nodo["derecha"])
    return recorrido_habilidades

def postorden(nodo): #defensivo
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades += postorden(nodo["izquierda"])
        recorrido_habilidades += postorden(nodo["derecha"])
        recorrido_habilidades.append(nodo["habilidad"])
    return recorrido_habilidades

#########torneo 
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

#########Peleas 1vs1

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

def definir_ninja_jugador(ninjaBuscado):
    """
    Retorna un diccionario con un ninja elejido por el jugador cuya clave es el nombre del ninja.
    Solo si este se encuentre en la lista registrada, de lo contrario retorna un diccionario vacio.

    ninjaBuscado: Es el nombre del ninja que se busca

    """
    ninjaEncontrado = encontrarNinja(ninjaBuscado, ninjas)
    if not ninjas:
        print('No hay ninjas registrados')
        return {}

    else:
        if ninjaEncontrado:
            return ninjaEncontrado
        elif not ninjaEncontrado:
            print('El ninja no esta registrados')
            return {}

def definir_ninja_maquina(ninjas_disponibles):
    """
    Retorna un diccionario con un ninja aleatorio que no ha sido seleccionado el jugador cuya clave es el nombre del ninja

    ninjas_disponibles: Es un diccionario

    """

    if not ninjas:
        print('No hay ninjas registrados')
        return {}
    else:
        ninjaAleatorio = random.choice(list(ninjas_disponibles.items()))
        diccionarioNinja = {ninjaAleatorio[0] : ninjaAleatorio[1]}
        return diccionarioNinja

def pvp():
    """
        Se encarga de administrar las peleas de un jugador y la computadora
    """

    ninjas_disponibles = estructuraDiccionarioNinjas
    while True:
        ninjaBuscado = input('Ingrese el ninja con el que desea combatir: ')

        if not ninjaBuscado:
            print('No puede dejar el campo en blanco: ')

        else:
            ninja_jugador = definir_ninja_jugador(ninjaBuscado)
            if ninja_jugador:
                del(ninjas_disponibles[ninja_jugador]) 
                break

    ninja_maquina = definir_ninja_maquina(ninjas_disponibles)    

    while True:
        try:
            print('1.- Ofensivo')
            print('2.- Equilibrado')
            print('1.- Defensivo')
            opcion = int(input('Ingrese la opcion de su ataque: '))

            if not opcion:
                print('No puede dejar el espacio en blanco.')

            elif not 1 <= opcion <= 3:
                print('Por favor ingrese un valor entre 1 y 3')
            else:
                break

        except ValueError:
            print('Por favor ingrese un numero entero entre 1-3')

    if opcion == 1:
        habilidadesJugador = inorden(estilos)

    elif opcion == 2:
        habilidadesJugador = preorden(estilos)

    elif opcion == 3:
        habilidadesJugador = postorden(estilos)

    pelea(ninja_jugador, ninja_maquina)

pvp()

               

import estructuras

#Pelear Contra Ninjas

def definir_ninja_jugador(ninjaBuscado):
    """
    Retorna un diccionario con un ninja elejido por el jugador cuya clave es el nombre del ninja.
    Solo si este se encuentre en la lista registrada, de lo contrario retorna un diccionario vacio.

    ninjaBuscado: Es el nombre del ninja que se busca

    """
    ninjaEncontrado = administracion.encontrarNinja(ninjaBuscado, ninjas)
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

#Comenzar Torneo

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


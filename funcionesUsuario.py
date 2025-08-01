import estructuras
import funcionesAdministrador
import archivos
import estructuras 
import funcionesPrincipales

import os
import random

ninjas = estructuras.diccionarioNinjas

def registrar_combate(ninja1, ninja2, ganador, usuario_email):
    archivo_jugador = f"combates_{usuario_email}.txt"

    # Leer conteo actual si el archivo existe
    ganados = 0
    perdidos = 0
    if os.path.exists(archivo_jugador):
        with open(archivo_jugador, "r") as archivo:
            for linea in archivo:
                if "Ganados" in linea:
                    partes = linea.strip().split("–")
                    if len(partes) >= 2:
                        stats = partes[1].strip()
                        try:
                            ganados = int(stats.split("ganados")[0].split(":")[1].strip())
                            perdidos = int(stats.split("ganados")[1].split("perdido")[0].strip())
                        except:
                            pass

    # Actualizar conteo
    if ganador == usuario_email:
        ganados += 1
    else:
        perdidos += 1

    # Sobrescribir archivo con nuevo resumen
    with open(archivo_jugador, "w") as archivo:
        archivo.write(f"Usuario: {usuario_email} – Combates: {ganados} ganados, {perdidos} perdido\n")

#Pelear Contra Ninjas

def definir_ninja_jugador(ninjaBuscado):
    """
    Retorna un diccionario con un ninja elejido por el jugador cuya clave es el nombre del ninja.
    Solo si este se encuentre en la lista registrada, de lo contrario retorna un diccionario vacio.

    ninjaBuscado: Es el nombre del ninja que se busca

    """
    ninjaEncontrado = funcionesAdministrador.encontrarNinja(ninjaBuscado, ninjas)
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

#Torneo

def listarNinjas():
    if not estructuras.diccionarioNinjas:
        print("No hay ninjas registrados.")
        return
    
    print(f"El numero de ninjas que hay es de {len(estructuras.diccionarioNinjas)}")
    print("Ordenar por:")
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

def calcular_puntaje_combate(nombre_ninja, rival_ninja):
    ninja_stats = estructuras.diccionarioNinjas[nombre_ninja]
    rival_stats = estructuras.diccionarioNinjas[rival_ninja]

    estilo = ninja_stats[3]
    base_puntos = ninja_stats[4]
    diferencia = base_puntos - rival_stats[4]

    if estilo == "Tanque":
        arbol = estructuras.estiloTanque_habilidades
    elif estilo == "Tirador":
        arbol = estructuras.estiloTirador_habilidades
    else:
        arbol = estructuras.estiloAsesino_habilidades

    if diferencia > 0:
        habilidades = estructuras.preorden(arbol)
        estrategia = "Ofensiva"
    elif diferencia == 0:
        habilidades = estructuras.inorden(arbol)
        estrategia = "Equilibrada"
    else:
        habilidades = estructuras.postorden(arbol)
        estrategia = "Defensiva"

    bonificacion = puntos_habilidad(arbol, habilidades)
    total = base_puntos + bonificacion

    return total, estrategia, bonificacion

def contar_victorias():
    victorias = {}

    if not os.path.exists("combates.txt"):
        return victorias

    with open("combates.txt", "r") as archivo:
        for linea in archivo:
            if "Ganador:" in linea:
                ganador = linea.strip().split("Ganador:")[1].strip()
                victorias[ganador] = victorias.get(ganador, 0) + 1
    return victorias

def quicksort_ranking(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1] < pivote[1]]
    mayores = [x for x in lista[1:] if x[1] >= pivote[1]]
    return quicksort_ranking(mayores) + [pivote] + quicksort_ranking(menores)

def mostrar_ranking():
    victorias = contar_victorias()
    ranking = list(victorias.items())
    ordenado = quicksort_ranking(ranking)

    print("\n--- Ranking de Ninjas por Victorias ---")
    for i, (ninja, wins) in enumerate(ordenado, start=1):
        print(f"{i}. {ninja}: {wins} victorias")

def pelea(ninja1,ninja2):
        datos1 = estructuras.diccionarioNinjas[ninja1]
        datos2 = estructuras.diccionarioNinjas[ninja2]
        print(f"{ninja1} VS {ninja2}")
        print(f"{ninja1}\nEstadisticas:\nFuerza: {datos1[0]}\nAgilidad: {datos1[1]}\nResistencia: {datos1[2]}\nEstilo de pelea: {datos1[3]}\nPuntos: {datos1[4]}\n")
        print(f"{ninja2}\nEstadisticas:\nFuerza: {datos2[0]}\nAgilidad: {datos2[1]}\nResistencia: {datos2[2]}\nEstilo de pelea: {datos2[3]}\nPuntos: {datos2[4]}\n")
        if estructuras.diccionarioNinjas[ninja1][4]<estructuras.diccionarioNinjas[ninja2][4]:
            print(f"{ninja2} es el ganador del enfrentamiento\n")
            return ninja2
        else:
            print(f"{ninja1} es el ganador del enfrentamiento\n")
            return ninja1
        
def torneoNinja():
    ninjas = list(estructuras.diccionarioNinjas.keys())
    if len(ninjas) < 2:
        print("No hay suficientes ninjas para el torneo.")
        return

    random.shuffle(ninjas)
    ronda = 1

    while len(ninjas) > 1:
        print(f"\n--- RONDA {ronda} ---")
        nuevos = []
        for i in range(0, len(ninjas), 2):
            if i+1 < len(ninjas):
                n1 = ninjas[i]
                n2 = ninjas[i+1]

                t1, e1, b1 = calcular_puntaje_combate(n1, n2)
                t2, e2, b2 = calcular_puntaje_combate(n2, n1)

                print(f"{n1} (estrategia {e1}, total {t1}) VS {n2} (estrategia {e2}, total {t2})")

                if t1 > t2:
                    ganador = n1
                elif t2 > t1:
                    ganador = n2
                else:
                    ganador = random.choice([n1, n2])
                    print("Empate técnico")

                print(f"→ Gana: {ganador}\n")
                nuevos.append(ganador)
        ninjas = nuevos
        ronda += 1

    print(f"\nGanador del torneo: {ninjas[0]}")

def pvp():
    usuario_email = funcionesPrincipales.obtener_email_usuario()
    nombre = input("Escriba el nombre de su ninja: ").strip()
    if nombre not in estructuras.diccionarioNinjas:
        print("Ese ninja no existe.")
        return

    oponente = random.choice([n for n in estructuras.diccionarioNinjas if n != nombre])
    print(f"Tu oponente será: {oponente}")

    total_jugador, estrategia_jugador, bono_jugador = calcular_puntaje_combate(nombre, oponente)
    total_oponente, estrategia_oponente, bono_oponente = calcular_puntaje_combate(oponente, nombre)

    print(f"\n{nombre} usa estrategia {estrategia_jugador} (+{bono_jugador} puntos)")
    print(f"{oponente} usa estrategia {estrategia_oponente} (+{bono_oponente} puntos)\n")

    print(f"{nombre} (Total: {total_jugador}) vs {oponente} (Total: {total_oponente})")

    if total_jugador > total_oponente:
        print(f"Ganador del combate: {nombre}")
    elif total_oponente > total_jugador:
        print(f"Ganador del combate: {oponente}")
    else:
        ganador = random.choice([nombre, oponente])
        print(f"Empate técnico. Ganador aleatorio: {ganador}")
    
    registrar_combate(nombre, oponente, ganador, usuario_email)

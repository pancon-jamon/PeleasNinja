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
"""

import os
import random
archivo = "habilidades_ninja.txt"

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


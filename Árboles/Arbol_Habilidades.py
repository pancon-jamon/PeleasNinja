#Árbol general de habilidades ninja
#con posibildidad de organizarse en preorden, inorden y postorden dependiendo de cómo vaya la pelea
import os
archivo = "habilidades_ninja.txt"

arbol_habilidades = {
    "habilidad":"Llama del Dragón",
    "izquierda":{"habilidad":"Muro de Viento Cortante",
                 "izquierda":{"habilidad":"Escudo de Sombras",
                              "izquierda":{"habilidad":"Curación del Fénix",
                                           "izquierda":None,"derecha":None
                                            },
                              "derecha":{"habilidad":"Trampa de Niebla",
                                         "izquierda":None,"derecha":None
                                        }
                  },
                 "derecha":{"habilidad":"Esquiva Fantasma",
                            "izquierda":{"habilidad":"Parada Perfecta",
                                         "izquierda":None,"derecha":None                                
                            },
                            "derecha":{"habilidad":"Ráfaga de Garras",
                                       "izquierda":None,"derecha":None
                                      }                     
                 }
    },
    "derecha":{"habilidad":"Puño del Tigre Feroz",
               "izquierda":{"habilidad":"Ataque Relámpago",
                            "izquierda":{"habilidad":"Tornado Sigiloso",
                                         "izquierda":None,"derecha":None
                            },
                            "derecha":{"habilidad":"Explosión Chakra",
                                       "izquierda":None,"derecha":None
                            }                   
                },
               "derecha":{"habilidad":"Golpe Rápido",
                          "izquierda":None,"derecha":None                   
               }
    }
}

def crear_archivo_habilidades():
    if not os.path.exists(archivo):
        with open("habilidades_ninja.txt", "w", encoding="utf-8") as file:
            file.write(str(arbol_habilidades))

crear_archivo_habilidades()

def inorden(nodo):
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades += inorden(nodo["izquierda"])
        recorrido_habilidades.append(nodo["habilidad"])
        recorrido_habilidades += inorden(nodo["derecha"])
    return recorrido_habilidades

def preorden(nodo):
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades.append(nodo["habilidad"])
        recorrido_habilidades += preorden(nodo["izquierda"])
        recorrido_habilidades += preorden(nodo["derecha"])
    return recorrido_habilidades

def postorden(nodo):
    recorrido_habilidades = []
    if nodo is not None:
        recorrido_habilidades += postorden(nodo["izquierda"])
        recorrido_habilidades += postorden(nodo["derecha"])
        recorrido_habilidades.append(nodo["habilidad"])
    return recorrido_habilidades

print("Técnica estratégica de pelea\n")
print("1. El ninja va ganando\n2. El ninja está empatado\n3. El ninja va perdiendo")
while True:
    try:
        habilidades_orden = int(input("Elija la técnica a ejecutar: "))
        print()
        if(habilidades_orden == 1):
            print("Técnica ofensiva:")
            pre_orden = preorden(arbol_habilidades)
            print(" → ".join(pre_orden))
            break
        elif(habilidades_orden == 2):
            print("Técnica de estrategia equilibrada:")
            in_orden = inorden(arbol_habilidades)
            print(" → ".join(in_orden))
            break
        elif(habilidades_orden == 3):
            print("Técnica defensiva:")
            in_orden = inorden(arbol_habilidades)
            print(" → ".join(in_orden))
            break
        else:
            print("Ingrese una técnica válida")
    except ValueError:
        print("Ingrese una técnica válida")

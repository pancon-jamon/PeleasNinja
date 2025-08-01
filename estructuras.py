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

diccionarioNinjas = {}

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

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


diccionarioNinjas = {
    "Naruto":{"Estilo":"Tanque","Habilidades":estiloTanque_habilidades},
    "Sasuke":{"Estilo":"Asesino","Habilidades":estiloAsesino_habilidades},
    }
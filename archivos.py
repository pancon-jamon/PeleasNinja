import os
import estructuras
archivo = "habilidades_ninja.txt"

def crearArchivoUsuarios():
    if os.path.isfile("usuarios.txt"):
        pass
    else:
        with open("usuarios.txt","w"):
            pass

def crearArchivoHabilidades():
    if not os.path.exists(archivo):
        with open(archivo, "w", encoding="utf-8") as file:
            file.write("Estilo de pelea Tirador:\n")
            file.write(str(estructuras.estiloTirador_habilidades))
            file.write("\nEstilo de pelea Asesino:\n")
            file.write(str(estructuras.estiloAsesino_habilidades))
            file.write("\nEstilo de pelea Tanque:\n")
            file.write(str(estructuras.estiloTanque_habilidades))

def guardarHabilidades():
    if os.path.exists(archivo):
        with open(archivo,"w",encoding="utf-8") as file:
            file.write("Estilo de pelea Tirador:\n")
            file.write(str(estructuras.estiloTirador_habilidades))
            file.write("\nEstilo de pelea Asesino:\n")
            file.write(str(estructuras.estiloAsesino_habilidades))
            file.write("\nEstilo de pelea Tanque:\n")
            file.write(str(estructuras.estiloTanque_habilidades))

def crearArchivosNinjas():
    if os.path.isfile("ninjas.txt"):
        pass
    else:
        with open("ninjas.txt",'w'):
            pass

def cargarNinjas():
    if os.path.exists("ninjas.txt"):
        with open("ninjas.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                nombre = datos[0]
                estilo = datos[1]
                fuerza = datos[2]
                agilidad = datos[3]
                resistencia = datos[4]
                arbol=datos[5]
                puntos = int(datos[6])
                estructuras.diccionarioNinjas[nombre] = {"Estilo":estilo,
                                             "Estadisticas":{'fuerza':fuerza,
                                                             'agilidad':agilidad,
                                                             'resistencia':resistencia},
                                             "Habilidades":arbol,
                                             "Puntos":puntos}

def guardarNinjas():
    with open("ninjas.txt", "w") as f:
        for ninja in estructuras.diccionarioNinjas.items():
            f.write(f"{ninja[0]}|"
                    f"{ninja[1]['Estilo']}|"
                    f"{ninja[1]['Estadisticas']['fuerza']}|"
                    f"{ninja[1]['Estadisticas']['agilidad']}|"
                    f"{ninja[1]['Estadisticas']['resistencia']}|"
                    f"{ninja[1]['Habilidades']}|"
                    f"{ninja[1]['Puntos']}\n")
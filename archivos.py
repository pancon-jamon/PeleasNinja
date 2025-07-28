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
                estructuras.diccionarioNinjas[nombre] = [fuerza, agilidad, resistencia, estilo, puntos]

def guardarNinja(nombre, características):
    with open("ninjas.txt", "a") as f:
        f.write(f"{nombre}|{características[0]}|{características[1]}|{características[2]}|{características[3]}|{características[4]}\n")
import os
import estructuras
archivo_habilidades = "Archivos/habilidades_ninja.txt"
archivo_ninjas = "Archivos/ninjas.txt"

def crearArchivoUsuarios():
    if not os.path.exists("usuarios.txt"):
        open("usuarios.txt", "w").close()
        

def crearArchivoHabilidades():
    if not os.path.exists(archivo_habilidades):
        with open(archivo_habilidades, "w", encoding="utf-8") as file:
            file.write("Estilo de pelea Tirador:\n")
            file.write(str(estructuras.estiloTirador_habilidades))
            file.write("\nEstilo de pelea Asesino:\n")
            file.write(str(estructuras.estiloAsesino_habilidades))
            file.write("\nEstilo de pelea Tanque:\n")
            file.write(str(estructuras.estiloTanque_habilidades))

def cargarNinjas():
    if os.path.exists(archivo_ninjas):
        with open(archivo_ninjas, "r") as archivo:
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
    with open(archivo_ninjas, "a") as f:
        f.write(f"{nombre}|{características[0]}|{características[1]}|{características[2]}|{características[3]}|{características[4]}\n")

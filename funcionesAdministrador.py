import estructuras

#Agregar Ninja
def agregarNinja():
    nombre = input("Nombre del ninja: ").strip()
    if nombre in estructuras.diccionarioNinjas:
        print("Ese ninja ya está registrado.")
        return
    try:
        fuerza = int(input("Fuerza (0-100): "))
        agilidad = int(input("Agilidad (0-100): "))
        resistencia = int(input("Resistencia (0-100): "))
        estilo = input("Estilo de pelea: ").strip()
        puntos = int(input("Puntos iniciales: "))
    except ValueError:
        print("Error ingrese valores válidos.")
        return

    estructuras.diccionarioNinjas[nombre] = [fuerza, agilidad, resistencia, estilo, puntos]
    print(f"Ninja {nombre} agregado con éxito.")

def buscarNinja():
    while True:
        print("1. Buscar por Nombre")
        print("2. Buscar por Estilos")
        print("3. Cancelar")
        opcion = input("Escriba como buscar: ")
        match opcion:
            case '1':
                ninjaBuscar = input("Escriba el Nombre del ninja a buscar: ")
                if not ninjaBuscar:
                    print('El campo no puede estar vacío. Inténtelo nuevamente')
                    continue
                else:
                    return ninjaBuscar
            case '2':
                    print("1. Tanque")
                    print("2. Asesino")
                    print("3. Tirador")
                    cualEstilo = input("Cual estilo quiere filtrar (1, 2, 3): ")
                    match cualEstilo:
                        case '1':
                            estilo = "Tanque"
                        case '2':
                            estilo = "Asesino"
                        case '3':
                            estilo = "Tirador"
                        case _:
                            print ("Error Estilo Invaido")
                            continue
                    for ninja in estructuras.diccionarioNinjas.items():
                        for datos in ninja[1].items():
                            if estilo == datos[1]:
                                print(f"Ninja: {ninja[0]} Estilo: {datos[1]}\n")

#Actualziar Ninja
#def actualizarNinja(actualizarNinja):

#Consultar Ninja
def consultarNinja(consultarNinja):
    ninja_encontrado = False  # Bandera para saber si lo encontramos
    for nombreNinja, habilidadesNinja in estructuras.diccionarioNinjas.items():
        if consultarNinja == nombreNinja.lower():  # Comparación en minúsculas
            ninja_encontrado = True
            # Asumo que habilidadesNinja es [fuerza, agilidad, resistencia, estilo, puntos]
            return (
                f'Nombre del ninja: {nombreNinja}\n'
                f'Fuerza: {habilidadesNinja[0]}\n'
                f'Agilidad: {habilidadesNinja[1]}\n'
                f'Resistencia: {habilidadesNinja[2]}\n'
                f'Estilo: {habilidadesNinja[3]}\n'
                f'Puntos: {habilidadesNinja[4]}'
            )
    if not ninja_encontrado:  # Solo muestra el error si no se encontró después de buscar todos
        print('El ninja no está registrado en este sistema.')

#Elimianr Ninja
def eliminarNinja(eliminarNinja):
    if eliminarNinja not in estructuras.diccionarioNinjas.keys():
        print("Ninja no encontrado")
    for ninja in estructuras.diccionarioNinjas:
        if ninja == eliminarNinja:
            estructuras.diccionarioNinjas.pop(ninja)
            break

#Crear Habilidades de Ninja

#Guardar Cambios
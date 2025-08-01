import estructuras
import archivos
import random

#Agregar Ninja
estilos = {"Tirador":estructuras.estiloTirador_habilidades,
           "Asesino":estructuras.estiloAsesino_habilidades,
           "Tanque":estructuras.estiloTanque_habilidades}

def agregarNinja():
    try:
        nombre = input("Nombre del ninja: ").strip()
        if nombre in estructuras.diccionarioNinjas:
            print("Ese ninja ya está registrado.")
            return
        estilo,arbol = random.choice(list(estilos.items()))
        fuerza = random.randint(5,10)
        agilidad = random.randint(5,10)
        resistencia = random.randint(5,10)
        puntos = fuerza + agilidad + resistencia

    except ValueError:
        print("Error ingrese valores válidos.")
        return

    estructuras.diccionarioNinjas[nombre] = {"Estilo":estilo,
                                             "Estadisticas":{'fuerza':fuerza,
                                                             'agilidad':agilidad,
                                                             'resistencia':resistencia},
                                             "Habilidades":arbol,
                                             "Puntos":puntos}
    archivos.guardarNinjas()
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
            case '3':
                print("Saliendo")
                break
            case _:
                print("Elija una opcion valida")

#Actualziar Ninja
def actualizarNinja(actualizarNinja):
    if not actualizarNinja:
        print("Cancelando")
    if actualizarNinja not in estructuras.diccionarioNinjas.keys():
        print("Ninja no encontrado")
    else:
        while True:
            try:
                print("Editar ninja")
                nou_fuerza = int(input("Escriba la nueva fuerza: "))
                nou_agilidad =int(input("Escriba la nueva agilidad: "))
                nou_resistencia = int(input("Escriba la nueva resistencia: "))
            except ValueError:
                print("Escriba una estadistica valida")
            if 5<=nou_fuerza<=10 and 5<=nou_agilidad<=10 and 5<=nou_resistencia<=10:
                estructuras.diccionarioNinjas[actualizarNinja]['Estadisticas'] = {
                    'fuerza':nou_fuerza,
                    'agilidad':nou_agilidad,
                    'resistencia':nou_resistencia
                }
                break
            else:
                print("Las estadisticas tiene que estar entre 5 y 10 ")
        archivos.guardarNinjas()
        print("Ninja actualizado con exito")
    

#Consultar Ninja
def consultarNinja(consultarNinja):
    if not consultarNinja:
        print("Cancelando")
    ninja_encontrado = False  # Bandera para saber si lo encontramos
    for nombreNinja, datos in estructuras.diccionarioNinjas.items():
        if consultarNinja.lower() == nombreNinja.lower():  # Comparación en minúsculas
            ninja_encontrado = True
            print (
                f'Ninja: {nombreNinja}\n'
                f'Estilo: {datos['Estilo']}\n'
                f'Fuerza: {datos['Estadisticas']['fuerza']}\n'
                f'Agilidad: {datos['Estadisticas']['agilidad']}\n'
                f'Resistencia: {datos['Estadisticas']['resistencia']}\n'
                f'Habilidades: {estructuras.preorden(estilos[datos['Estilo']])}'
            )
    if not ninja_encontrado:  # Solo muestra el error si no se encontró después de buscar todos
        print('El ninja no está registrado en este sistema.')

#Elimianr Ninja
def eliminarNinja(eliminarNinja):
    if not eliminarNinja:
        print("Cancelando")
    if eliminarNinja not in estructuras.diccionarioNinjas.keys():
        print("Ninja no encontrado")
    for ninja in estructuras.diccionarioNinjas:
        if ninja == eliminarNinja:
            estructuras.diccionarioNinjas.pop(ninja)
            break
    archivos.guardarNinjas()

#Crear Habilidades de Ninja
def crearHabilidadNinja():
    while True:
        print("1. Tanque" \
        "\n2. Asesino" \
        "\n3. Tirador")
        opcion = input("Elija elestilo al cual añadirle la habilidad :")
        match opcion:
            case '1':
                print("Estilo Tanque")
                nombre = input("Escriba el nombre del la habilidad: ")
                puntos = random.randint(1,5)
                nou_habilidad = {"habilidad":nombre,
                              "puntos":puntos,
                              "izquierda":None,"derecha":None}
                def recorrer(nodo):
                    completado = False
                    if nodo is None or completado:
                        return
                    if nodo['izquierda'] is None:
                        nodo ['izquierda']=[nou_habilidad]
                        completado = True
                        return
                    if nodo['derecha'] is None:
                        nodo['derecha']=[nou_habilidad]
                        completado = True
                        return
                    recorrer(nodo['izquierda'])
                    recorrer(nodo['derecha'])
                recorrer(estructuras.estiloTanque_habilidades)
                break
            case '2':
                print("Estilo Asesino")
                nombre = input("Escriba el nombre del la habilidad: ")
                puntos = random.randint(1,5)
                nou_habilidad = {"habilidad":nombre,
                              "puntos":puntos,
                              "izquierda":None,"derecha":None}
                def recorrer(nodo):
                    completado = False
                    if nodo is None or completado:
                        return
                    if nodo['izquierda'] is None:
                        nodo ['izquierda']=[nou_habilidad]
                        completado = True
                        return
                    if nodo['derecha'] is None:
                        nodo['derecha']=[nou_habilidad]
                        completado = True
                        return
                    recorrer(nodo['izquierda'])
                    recorrer(nodo['derecha'])
                recorrer(estructuras.estiloAsesino_habilidades)
                break
            case '3':
                print("Estilo Tirador")
                nombre = input("Escriba el nombre del la habilidad: ")
                puntos = random.randint(1,5)
                nou_habilidad = {"habilidad":nombre,
                              "puntos":puntos,
                              "izquierda":None,"derecha":None}
                def recorrer(nodo):
                    completado = False
                    if nodo is None or completado:
                        return
                    if nodo['izquierda'] is None:
                        nodo ['izquierda']=[nou_habilidad]
                        completado = True
                        return
                    if nodo['derecha'] is None:
                        nodo['derecha']=[nou_habilidad]
                        completado = True
                        return
                    recorrer(nodo['izquierda'])
                    recorrer(nodo['derecha'])
                recorrer(estructuras.estiloTirador_habilidades)
                break
            case _:
                print('Elija una ocion valida')
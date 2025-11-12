# Importamos las validaciones porque las necesitaremos
import validaciones

# --- Función Auxiliar para Imprimir ---
def _mostrar_lista_paises(lista_paises, mensaje_cabecera):
    """
    Función interna para mostrar una lista de países de forma ordenada.
    Se usará en búsquedas, filtros y ordenamientos.
    """
    if not lista_paises: # Si la lista de resultados está vacía
        print("No se encontraron países que cumplan con el criterio.")
        return

    print(mensaje_cabecera)
    for pais in lista_paises:
        print(f"  - Nombre: {pais['nombre']}")
        print(f"    Población: {pais['poblacion']}")
        print(f"    Superficie: {pais['superficie']} km²")
        print(f"    Continente: {pais['continente']}")
        print("--------------------") # Separador

# --- Opción 2 ---
def agregar_pais(paises):
    """
    Pide al usuario los datos de un nuevo país, valida que el nombre no
    se repita, crea el diccionario y lo agrega a la lista.
    """
    print("\n--- 2. Agregar Nuevo País ---")
    
    nombre = validaciones.validar_texto_no_vacio("Ingrese el nombre del país: ")
    
    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya existe en la lista.")
            encontrado = True
            break 
            
    if not encontrado:
        poblacion = validaciones.validar_entero_positivo("Ingrese la población: ")
        superficie = validaciones.validar_entero_positivo("Ingrese la superficie (km²): ")
        continente = validaciones.validar_texto_no_vacio("Ingrese el continente: ")
        
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        
        paises.append(nuevo_pais)
        print(f"¡País '{nombre}' agregado exitosamente!")

    return paises

# --- Opción 3 ---
def actualizar_pais(paises):
    """
    Pide un nombre, busca el país y actualiza su población y superficie.
    """
    print("\n--- 3. Actualizar Datos de un País ---")
    
    nombre_buscado = validaciones.validar_texto_no_vacio("Ingrese el nombre del país que desea actualizar: ")
    
    encontrado = False
    
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            encontrado = True
            
            print(f"País encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']} km²")
            
            nueva_poblacion = validaciones.validar_entero_positivo("Ingrese la nueva población: ")
            nueva_superficie = validaciones.validar_entero_positivo("Ingrese la nueva superficie (km²): ")
            
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            
            print(f"¡Datos de '{pais['nombre']}' actualizados exitosamente!")
            break 

    if not encontrado:
        print(f"Error: No se encontró ningún país con el nombre '{nombre_buscado}'.")

    return paises

# --- Opción 4 ---
def buscar_pais(paises):
    """
    Pide un término de búsqueda y muestra todos los países
    cuyo nombre contenga ese término (búsqueda parcial).
    """
    print("\n--- 4. Buscar un País por Nombre ---")
    
    termino_buscado = input("Ingrese el nombre (o parte del nombre) del país a buscar: ").lower()
    
    resultados_encontrados = []
    
    for pais in paises:
        if termino_buscado in pais["nombre"].lower():
            resultados_encontrados.append(pais)
            
    _mostrar_lista_paises(resultados_encontrados, f"\n--- Resultados de la búsqueda para '{termino_buscado}' ---")

# --- Opción 5 ---
def menu_filtrar(paises):
    """
    Muestra un submenú para elegir el tipo de filtro
    y llama a la función correspondiente.
    """
    print("\n--- 5. Filtrar Países ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    print("4. Volver al menú principal")

    opcion = validaciones.validar_entero_positivo("Seleccione una opción (1-4): ")

    if opcion == 1:
        _filtrar_por_continente(paises)
    elif opcion == 2:
        _filtrar_por_poblacion(paises)
    elif opcion == 3:
        _filtrar_por_superficie(paises)
    elif opcion == 4:
        print("Volviendo al menú principal...")
# Importamos las validaciones porque las necesitaremos
import validaciones

# --- FUNCIONES AUXILIARES (Para imprimir y ordenar) ---

def _mostrar_lista_paises(lista_paises, mensaje_cabecera):
    """
    Función interna para mostrar una lista de países de forma ordenada.
    """
    if not lista_paises:
        print("No se encontraron países que cumplan con el criterio.")
        return

    print(mensaje_cabecera)
    for pais in lista_paises:
        print(f"  - Nombre: {pais['nombre']}")
        print(f"    Población: {pais['poblacion']}")
        print(f"    Superficie: {pais['superficie']} km²")
        print(f"    Continente: {pais['continente']}")
        print("--------------------")

def _obtener_nombre(pais):
    """Devuelve el nombre en minúsculas para ordenar."""
    return pais['nombre'].lower()

def _obtener_poblacion(pais):
    """Devuelve la población para ordenar."""
    return pais['poblacion']

def _obtener_superficie(pais):
    """Devuelve la superficie para ordenar."""
    return pais['superficie']

# --- FIN FUNCIONES AUXILIARES ---

# --- Opción 2 ---
def agregar_pais(paises):
    print("\n--- 2. Agregar Nuevo País ---")
    nombre = validaciones.validar_texto_no_vacio("Ingrese el nombre del país: ")
    
    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya existe en la lista.")
            encontrado = True
            break 
            
    if not encontrado:
        poblacion = validaciones.validar_entero_positivo("Ingrese la población: ")
        superficie = validaciones.validar_entero_positivo("Ingrese la superficie (km²): ")
        continente = validaciones.validar_texto_no_vacio("Ingrese el continente: ")
        
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(nuevo_pais)
        print(f"¡País '{nombre}' agregado exitosamente!")
    return paises

# --- Opción 3 ---
def actualizar_pais(paises):
    print("\n--- 3. Actualizar Datos de un País ---")
    nombre_buscado = validaciones.validar_texto_no_vacio("Ingrese el nombre del país que desea actualizar: ")
    encontrado = False
    
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            encontrado = True
            print(f"País encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']} km²")
            
            pais["poblacion"] = validaciones.validar_entero_positivo("Ingrese la nueva población: ")
            pais["superficie"] = validaciones.validar_entero_positivo("Ingrese la nueva superficie (km²): ")
            print(f"¡Datos de '{pais['nombre']}' actualizados exitosamente!")
            break 

    if not encontrado:
        print(f"Error: No se encontró ningún país con el nombre '{nombre_buscado}'.")
    return paises

# --- Opción 4 ---
def buscar_pais(paises):
    print("\n--- 4. Buscar un País por Nombre ---")
    termino_buscado = input("Ingrese el nombre (o parte del nombre) del país a buscar: ").lower()
    resultados = []
    for pais in paises:
        if termino_buscado in pais["nombre"].lower():
            resultados.append(pais)
    _mostrar_lista_paises(resultados, f"\n--- Resultados de la búsqueda para '{termino_buscado}' ---")

# --- Opción 5 ---
def menu_filtrar(paises):
    print("\n--- 5. Filtrar Países ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango de Población")
    print("3. Filtrar por Rango de Superficie")
    print("4. Volver al menú principal")
    opcion = validaciones.validar_entero_positivo("Seleccione una opción (1-4): ")

    if opcion == 1: _filtrar_por_continente(paises)
    elif opcion == 2: _filtrar_por_poblacion(paises)
    elif opcion == 3: _filtrar_por_superficie(paises)
    elif opcion == 4: print("Volviendo al menú principal...")
    else: print("Error: Opción no válida (1-4).")

def _filtrar_por_continente(paises):
    cont = validaciones.validar_texto_no_vacio("Ingrese el continente a filtrar: ").lower()
    res = []
    for pais in paises:
        if pais["continente"].lower() == cont:
            res.append(pais)
    _mostrar_lista_paises(res, f"\n--- Países en '{cont}' ---")

def _filtrar_por_poblacion(paises):
    print("--- Filtrar por Rango de Población ---")
    min_v = validaciones.validar_entero_positivo("Mínimo: ")
    max_v = validaciones.validar_entero_positivo("Máximo: ")
    if min_v > max_v:
        print("Error: El mínimo no puede ser mayor al máximo.")
        return
    res = []
    for p in paises:
        if min_v <= p["poblacion"] <= max_v:
            res.append(p)
    _mostrar_lista_paises(res, f"\n--- Países con población entre {min_v} y {max_v} ---")

def _filtrar_por_superficie(paises):
    print("--- Filtrar por Rango de Superficie ---")
    min_v = validaciones.validar_entero_positivo("Mínima (km²): ")
    max_v = validaciones.validar_entero_positivo("Máxima (km²): ")
    if min_v > max_v:
        print("Error: El mínimo no puede ser mayor al máximo.")
        return
    res = []
    for p in paises:
        if min_v <= p["superficie"] <= max_v:
            res.append(p)
    _mostrar_lista_paises(res, f"\n--- Países con superficie entre {min_v} y {max_v} km² ---")

# --- Opción 6 (SIN LAMBDA) ---
def menu_ordenar(paises):
    print("\n--- 6. Ordenar Países ---")
    print("1. Por Nombre (A-Z)")
    print("2. Por Nombre (Z-A)")
    print("3. Por Población (Menor a Mayor)")
    print("4. Por Población (Mayor a Menor)")
    print("5. Por Superficie (Menor a Mayor)")
    print("6. Por Superficie (Mayor a Menor)")
    print("7. Volver al menú principal")
    op = validaciones.validar_entero_positivo("Seleccione una opción (1-7): ")

    lista_ord = paises.copy()
    msg = ""

    if op == 1:
        lista_ord.sort(key=_obtener_nombre, reverse=False)
        msg = "\n--- Países Ordenados por Nombre (A-Z) ---"
    elif op == 2:
        lista_ord.sort(key=_obtener_nombre, reverse=True)
        msg = "\n--- Países Ordenados por Nombre (Z-A) ---"
    elif op == 3:
        lista_ord.sort(key=_obtener_poblacion, reverse=False)
        msg = "\n--- Países Ordenados por Población (Menor a Mayor) ---"
    elif op == 4:
        lista_ord.sort(key=_obtener_poblacion, reverse=True)
        msg = "\n--- Países Ordenados por Población (Mayor a Menor) ---"
    elif op == 5:
        lista_ord.sort(key=_obtener_superficie, reverse=False)
        msg = "\n--- Países Ordenados por Superficie (Menor a Mayor) ---"
    elif op == 6:
        lista_ord.sort(key=_obtener_superficie, reverse=True)
        msg = "\n--- Países Ordenados por Superficie (Mayor a Menor) ---"
    elif op == 7:
        return
    else:
        print("Error: Opción no válida (1-7).")
        return

    _mostrar_lista_paises(lista_ord, msg)
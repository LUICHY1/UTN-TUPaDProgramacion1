def mostrar_estadisticas(paises):

    print("\n--- 7. Estadísticas ---")

    # Validación de seguridad (aunque Main.py ya lo hace)
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    # 1. Inicializamos variables para max/min
    # Tomamos el primer país como referencia inicial
    pais_max_pob = paises[0]
    pais_min_pob = paises[0]
    
    total_poblacion = 0
    total_superficie = 0
    
    # 2. Diccionario para contar países por continente
    conteo_continentes = {}

    # 3. Recorremos la lista UNA SOLA VEZ para ser eficientes
    for pais in paises:
        
        # --- Cálculo de Max/Min ---
        if pais["poblacion"] > pais_max_pob["poblacion"]:
            pais_max_pob = pais
        
        if pais["poblacion"] < pais_min_pob["poblacion"]:
            pais_min_pob = pais
        
        # --- Suma para promedios ---
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
        
        # --- Conteo por continente ---
        continente = pais["continente"]
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    # --- Fin del bucle ---
    
    # 4. Cálculos finales
    cantidad_paises = len(paises)
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises

    # --- 5. Impresión de resultados ---
    print("\n--- Estadísticas Globales ---")
    
    print("\n1. Población:")
    print(f"  - País con mayor población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:_} hab.)")
    print(f"  - País con menor población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:_} hab.)")
    # Usamos f-string :_ para separar los miles (ej: 1_000_000)
    # y :.2f para mostrar 2 decimales
    print(f"  - Promedio de población: {promedio_poblacion:,.2f} habitantes.")
    
    print("\n2. Superficie:")
    print(f"  - Promedio de superficie: {promedio_superficie:,.2f} km².")
    
    print("\n3. Países por Continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad} país(es)")
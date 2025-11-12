import os 

# Esto calcula la ruta absoluta de la carpeta DONDE ESTÁ este archivo .py
_script_dir = os.path.dirname(os.path.abspath(__file__))
# --------------------

def cargar_datos(nombre_archivo):

    lista_paises = []
    
    # Unimos la ruta del script con el nombre del archivo
    ruta_completa = os.path.join(_script_dir, nombre_archivo)
    # ------------------------
    
    # 1. Validación de existencia (ahora usa la ruta completa)
    if not os.path.exists(ruta_completa):
        # Mostramos la ruta completa para que sea más fácil depurar
        print(f"Error: El archivo '{ruta_completa}' no se encuentra.")
        return lista_paises 

    # 2. Lectura del archivo (ahora usa la ruta completa)
    archivo = open(ruta_completa, 'r', encoding='utf-8')
    cabecera = archivo.readline()
    lineas = archivo.readlines()
    archivo.close()

    # 3. Procesamiento de cada línea (esto sigue igual)
    for linea in lineas:
        linea = linea.strip() 

        if not linea: 
            continue

        partes = linea.split(',')

        if len(partes) == 4:

            nombre = partes[0].strip() 
            poblacion_str = partes[1].strip()
            superficie_str = partes[2].strip()
            continente = partes[3].strip()

            if (poblacion_str.isdigit() and superficie_str.isdigit() and 
                nombre and continente):

                pais = {
                    "nombre": nombre,
                    "poblacion": int(poblacion_str),
                    "superficie": int(superficie_str), 
                    "continente": continente
                }
                lista_paises.append(pais)
            else:
                print(f"Error de formato en datos: '{linea}'. Se omite.")
        else:
            print(f"Error de formato en línea (columnas != 4): '{linea}'. Se omite.")

    return lista_paises
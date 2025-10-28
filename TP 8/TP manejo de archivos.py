# Ejercicio 1: Crear archivo inicial
print("Creando archivo productos.txt con datos iniciales...")
try:
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera, 120.5,30\n")
        archivo.write("Cuaderno,300.0,15\n")
        archivo.write("Goma,80.0,50\n")
        print("Archivo 'productos.txt' creado exitosamente.")
except IOError as e:
    print(f"Error al crear el archivo: {e}")
print("-" * 30)

# Ejercicio 2: Leer y mostrar productos
print("Leyendo y mostrando productos desde productos.txt...")
try:
    with open("productos.txt", "r") as archivo:
        print("Productos en el archivo")
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            if len(partes) == 3:
                nombre = partes[0]
                try:
                    precio = float(partes[1])
                    cantidad = int(partes[2])
                    print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
                except ValueError:
                    print(f"Error al procesar datos numéricos en línea: '{linea_limpia}'")
            elif linea_limpia:
                print(f"Línea con formato incorrecto ignorada: '{linea_limpia}'")
except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no existe. Ejecuta el paso 1 primero.")
except IOError as e:
    print(f"Error al leer el archivo: {e}")
print("-" * 30)

# Ejercicio 3: Agregar producto desde teclado
print("Agregando nuevo producto...")
try:
    while True:
        nombre_nuevo = input("Ingrese nombre del nuevo producto: ")
        if nombre_nuevo.strip():
            nombre_nuevo = nombre_nuevo.strip()
            break
    else:
        print("El nombre no puede estar vacío. Intente de nuevo.")
    while True:
        try:
            precio_nuevo = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Precio inválido. Ingrese un número.")
    while True:
        try:
            Cantidad_nueva = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Cantidad inválida. Ingrese un número entero.")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre_nuevo}, {precio_nuevo},{Cantidad_nueva}\n")
    print(f"Producto '{nombre_nuevo}' agregado exitosamente.")
except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no existe. No se puede agregar.")
except IOError as e:
    print(f"Error al agregar al archivo: {e}")
print("-" * 30)

# Ejercicio 4: Cargar productos en lista de diccionarios
print("Cargando productos en una lista de diccionarios...")
productos = []
try:
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            partes = linea_limpia.split(",")
            if len(partes) == 3:
                try:
                    producto_dict = {
                        "nombre": partes[0],
                        "precio": float(partes[1]),
                        "cantidad": int(partes[2])
                    }
                    productos.append(producto_dict)
                except ValueError:
                    print(f"Error al convertir datos númericos en línea: '{linea_limpia}'")
            elif linea_limpia:
                print(f"Línea con formato incorrecto ignorada: '{linea_limpia}'")
    print(f"Productos cargados en la lista: {len(productos)} encontrados.")
except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no existe.")
except IOError as e:
    print(f"Error al leer el archivo: {e}")
print("-" * 30)

# Ejercicio 5: Buscar producto por nombre
if not productos:
    print("No hay productos cargados para buscar.")
else:
    print("Buscando producto por nombre...")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("\n--Producto encontrado--")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print(f"Producto '{nombre_buscar}' no encontrado.")
print("-" * 30)

# Ejercicio 6: Guardar productos actualizados
if not productos:
    print("No hay productos en memoria para guardar.")
else:
    print("Guardando productos actualizados en productos.txt...")
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                linea_guardar = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea_guardar)
        print("Archivo 'productos.txt' actualizado correctamente.")
    except IOError as e:
        print(f"Error al guardar en el archivo: {e}")
print("-" * 30)
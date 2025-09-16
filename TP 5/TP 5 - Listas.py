#Actividad 1
notas = [7.5, 8.0, 6.3, 9.1, 5.5, 8.7, 7.8, 6.9, 9.5, 7.2]
print("Notas de los estudiantes:")
for i, nota in enumerate(notas, start=1):
    print(f"Estudiante {i}: {nota}")
promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"\nPromedio de notas: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
nota_aprobacion = 6.0
aprobados = [nota for nota in notas if nota >= nota_aprobacion]
print(f"\nCantidad de estudiantes que aprobaron: {len(aprobados)}")
desaprobados = [nota for nota in notas if nota < nota_aprobacion]
print(f"Cantidad de estudiantes que desaprobaron: {len(desaprobados)}")
print("Notas de estudiantes desaprobados:")
for i, nota in enumerate(desaprobados, start=1):
    print(f"Desaprobado {i}: {nota}")


#Actividad 2
productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for producto in productos_ordenados:
    print(producto)
producto_a_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("\nLista actualizada de productos:")
    for producto in productos:
        print(producto)
else:
    print("\nEl producto no se encuentra en la lista.")


#Actividad 3
import random
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Lista original de números:")
print(numeros)
print("\nNúmeros pares:")
print(pares)
print(f"Cantidad de números pares: {len(pares)}")
print("\nNúmeros impares:")
print(impares)
print(f"Cantidad de números impares: {len(impares)}")


#Actividad 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = list(set(datos))
print("Lista original:", datos)
print("Lista sin elementos repetidos:", datos_sin_repetidos)

#Actividad 5

estudiantes = ["Ana", "Bruno", "Carla", "David", "Elena", "Fernando", "Gabriela", "Hugo"]
print("Lista de estudiantes presentes:")
for estudiante in estudiantes:
    print("-", estudiante)
accion = input("\n¿Deseas agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ").strip().lower()
if accion == "agregar":
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ").strip()
    estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista.")
elif accion == "eliminar":
    estudiante_a_eliminar = input("Ingresa el nombre del estudiante que deseas eliminar: ").strip()
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print(f"{estudiante_a_eliminar} ha sido eliminado de la lista.")
    else:
        print(f"{estudiante_a_eliminar} no se encuentra en la lista.")
else:
    print("Opción no válida. No se realizaron cambios.")
print("\nLista final de estudiantes:")
for estudiante in estudiantes:
    print("-", estudiante)


#Actividad 6
numeros = [10, 20, 30, 40, 50, 60, 70]
rotada = [numeros[-1]] + numeros[:-1]
print("Lista original:", numeros)
print("Lista rotada una posición a la derecha:", rotada)


#Actividad 7
temperaturas = [
    [12, 22],  # Lunes
    [14, 25],  # Martes
    [13, 24],  # Miércoles
    [15, 28],  # Jueves
    [11, 21],  # Viernes
    [10, 20],  # Sábado
    [13, 27]   # Domingo
]
suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for i in range(len(temperaturas)):
    temp_min = temperaturas[i][0]
    temp_max = temperaturas[i][1]
    suma_min += temp_min
    suma_max += temp_max
    amplitud = temp_max - temp_min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)
print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}°C")
print(f"El día con mayor amplitud térmica fue {dia_mayor_amplitud} con {mayor_amplitud}°C de diferencia.")

#Actividad 8
notas = [
    [7.5, 8.0, 6.5],  # Estudiante 1
    [9.0, 7.5, 8.0],  # Estudiante 2
    [6.0, 5.5, 7.0],  # Estudiante 3
    [8.5, 9.0, 8.0],  # Estudiante 4
    [7.0, 6.5, 7.5]   # Estudiante 5
]
print("Promedio de cada estudiante:")
for i in range(len(notas)):
    promedio_estudiante = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i+1}: {promedio_estudiante:.2f}")
print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma_materia = sum(notas[i][j] for i in range(len(notas)))
    promedio_materia = suma_materia / len(notas)
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#Actividad 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()
print("Tablero inicial:")
mostrar_tablero(tablero)
for turno in range(1, 6): 
    for jugador in ["X", "O"]:
        print(f"Turno del jugador {jugador}")
        fila = int(input("Ingrese la fila (0, 1 o 2): "))
        columna = int(input("Ingrese la columna (0, 1 o 2): "))
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador
        else:
            print("Casilla ocupada. Intenta de nuevo.")
            fila = int(input("Ingrese la fila (0, 1 o 2): "))
            columna = int(input("Ingrese la columna (0, 1 o 2): "))
            tablero[fila][columna] = jugador
        mostrar_tablero(tablero)

#Actividad 10
ventas = [
    [10, 12, 9, 14, 11, 13, 15],   # Producto 1
    [8, 9, 10, 11, 12, 13, 14],     # Producto 2
    [5, 6, 7, 8, 9, 10, 11],        # Producto 3
    [20, 18, 22, 19, 21, 23, 24]    # Producto 4
]
print("Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total} unidades")
ventas_por_dia = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(7)]
dia_mayor_ventas = ventas_por_dia.index(max(ventas_por_dia)) + 1
print(f"\nEl día con mayores ventas totales fue el día {dia_mayor_ventas} con {max(ventas_por_dia)} unidades.")
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido} con {max(totales_productos)} unidades.")
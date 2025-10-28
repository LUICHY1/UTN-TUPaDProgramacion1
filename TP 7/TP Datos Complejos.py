# Diccionario Inicial.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# 1) Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario actualizado")
print(precios_frutas)

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario actualizado")
print(precios_frutas)

# 3) Crear una lista solo con las frutas (claves)
lista_de_frutas = list(precios_frutas.keys())
print("Lista de frutas")
print(lista_de_frutas)

# 4) Agenda Telefónica
contactos = {}
print("Carga de 5 contactos")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero
    print(f"Concatco '{nombre}' agregado.")
print("Agenda completa")
print(contactos)
print("Consulta de contactos")
nombre_consulta = input("Ingrese el nombre del contacto que desea buscar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto '{nombre_consulta}' no se encuentra en la agenda.")


# 5) Contador de palabras

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print(f"Recuento de palabras: {recuento}")

# 6) Promedio de notas de alumnos

alumnos = {}
print("Carga de 3 alumnos y sus notas")
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    notas_tupla = (nota1, nota2, nota3)
    alumnos[nombre] = notas_tupla
print("Promedio de cada alumno")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# 7) Operaciones con sets de estudiantes
parcial1 = {101, 102, 105, 107, 110}
parcial2 = {102, 103, 104, 107, 109}
print(f"Aprobados parcial 1: {parcial1}")
print(f"Aprobados Parcial 2: {parcial2}")
ambos_parciales = parcial1 & parcial2
print(f"Alumnos que aprobaron AMBOS parciales: {ambos_parciales}")
solo_un_parcial = parcial1 ^ parcial2
print(f"Alumnos que aprobaron SOLO UN parcial: {solo_un_parcial}")
todos_los_alumnos = parcial1 | parcial2
print(f"Lista total de alumnos que aprobaron AL MENOS UN parcial: {todos_los_alumnos}")


# 8) Gestión de stock
stock = {"lapiz": 10, "cuaderno": 5, "goma": 3}
print(f"Inventario inicial: {stock}")
while True:
    print("Menú de Gestión de Stock")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock / Añadir nuevo producto")
    print("3. Salir")
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ").lower()
        cantidad = stock.get(producto, "Producto no encontrado")
        if isinstance(cantidad, int):
            print(f"El stock de '{producto}' es: {cantidad} unidades.")
        else:
            print(f"'{producto}' no se encuentra en el inventario.")
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ").lower()
        try:
            cantidad_agregar = int(input(f"Ingrese la cantidad a agregar para '{producto}': "))
            stock[producto] = stock.get(producto, 0) + cantidad_agregar
            print(f"¡Stock actualizado! Nuevo total de '{producto}': {stock[producto]}")
            print(f"Inventario actual: {stock}")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break


# 9) Agenda con clave (dia, hora)
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:00"): "Turno médico",
    ("viernes", "18:00"): "Entrenamiento"
}
print("Consulta de Agenda")
print("Días/Horas con eventos:", list(agenda.keys()))
dia = input("Ingrese el día a consultar (ej: lunes): ").lower()
hora = input("Ingrese la ora a consultar (ej: 10:00): ")
clave_consulta = (dia, hora)
evento = agenda.get(clave_consulta, "No hay ningún evento agendado en esa fecha y hora.")
print(f"Evento para ({dia}, {hora}):")
print(evento)


# 10) Invertir un diccionario (país: capital -> capital: país)
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}
print(f"Diccionario original: {original}")
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(f"Diccionario invertido {invertido}")
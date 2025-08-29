
#Actividad 1

edad_input = input("Por favor, ingresa tu edad: ")
if edad_input.isdigit():
    edad = int(edad_input)
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("Entrada inválida. Por favor, ingrese un número")

#Actividad 2

nota_input = input("Por favor, ingresa tu nota: ")
if nota_input.isdigit():
    nota = int(nota_input)
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("Entrada inválida. Por favor, ingrese un número")

#Actividad 3

numero_input = input("Por favor, ingresa un número: ")
if numero_input.isdigit():
    numero = int(numero_input)
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
else:
    print("Entrada inválida. Por favor, ingreese un número")

#Actividad 4

edad_input = input("Por favor, ingresa tu edad: ")
if edad_input.isdigit():
    edad = int(edad_input)
    if edad < 12:
        print("Niño/a")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >= 18 and edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")
else:
    print("Entrada inválida. Por favor, ingrese un número")

#Actividad 5

contraseña = input("Por favor, ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6


import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
elif media == mediana and mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "No se puede determinar un sesgo claro"
print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Media: {media:.2f}, Mediana: {mediana}, Moda: {moda}")
print("Resultado del análisis de sesgo:", sesgo)

#Actividad 7


texto = input("Por favor, ingresa una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
    print("Resultado:", texto)
else:
    print("Resultado:", texto)

#Actividad 8

nombre = input("Por favor, ingresa tu nombre: ")
print("Selecciona una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")
opcion = input("Ingresa el número de la opción (1, 2 o 3): ")
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Por favor, ingresa 1, 2 o 3.")

#Actividad 9

magnitud_input = input("Ingrese la magnitud del terremoto: ")
try:
    magnitud = float(magnitud_input)
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número válido.")

#Actividad 10

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"
print("Estación del año:", estacion)
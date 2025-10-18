import math #Necesario para el Ejercicio 4
# Ejercicio 1
print("-Ejercicio 1-")
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo() #Llamada a la función

# Ejercicio 2
print("-Ejercicio 2-")
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("Introduce tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

# Ejercicio 3
print("-Ejercicio 3-")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nom = input("Introduce tu nombre: ")
ape = input("Introduce tu apellido: ")
ed = int(input("Introduce tu edad: "))
res = input("Introduce tu residencia: ")
informacion_personal(nom, ape, ed, res)

# Ejercicio 4
print("-Ejercicio 4-")
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio_circulo = float(input("Introduce el radio del círculo: "))
area = calcular_area_circulo(radio_circulo)
perimetro = calcular_perimetro_circulo(radio_circulo)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Ejercicio 5
print("-Ejercicio 5-")
def segundos_a_horas(segundos):
    return segundos / 3600
seg = int(input("Introduce una cantidad de segundos: "))
horas = segundos_a_horas(seg)
if horas == 1:
    print(f"{seg} segundos equivalen a 1 hora.")
else:
    print(f"{seg} segundos equivalen a {horas:.4} horas.")

# Ejercicio 6
print("-Ejercicio 6-")
def tabla_multiplicar(numero):
    print(F"-- Tabla de multiplicar del {numero} --")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
num_tabla = int(input("Introduce un número para ver su tabla: "))
tabla_multiplicar(num_tabla)

# Ejercicio 7
print("-Ejercicio 7-")
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)
num1 = float(input("Introduce el primer número (a): "))
num2 = float(input("Introduce el segundo número (b): "))
suma, resta, mult, div = operaciones_basicas(num1, num2)
print(f"Suma: {suma:g}")
print(f"Resta: {resta:g}")
print(f"Multiplicación: {mult:g}")
if num2 != 0:
    print(f"División: {div:g}")
else:
    print(f"División: {div}")

# Ejercicio 8
print("-Ejercicio 8-")
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso_kg = float(input("Introduce tu peso en kg: "))
altura_m = float(input("Introduce tu altura en metros (ej: 1.75): "))
imc = calcular_imc(peso_kg, altura_m)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Ejercicio 9
print("-Ejercicio 9-")
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Introduce la temperatura en grados Celsius: "))
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C equivalen a {temp_f:.2f}°F.")

# Ejercicio 10
print("-Ejercicio 10-")
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))
prom = calcular_promedio(n1, n2, n3)
print(f"El promedio de los tres números es: {prom:g}")
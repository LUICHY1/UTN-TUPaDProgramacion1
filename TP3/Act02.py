#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingresa un número entero: ")
if numero.startswith('-'):
    numero = numero[1:]
cantidad_digitos = len(numero)
print("El número tiene", cantidad_digitos, "dígito(s).")
#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma_total = 0
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero == 0:
        break  
    suma_total += numero  
print("La suma total de los números ingresados es:", suma_total)
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
total = 0 
print("Ingresa números enteros para sumarlos. Ingresa 0 para finalizar.")
while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:  
        break
    total += numero 
print(f"El total acumulado es: {total}")

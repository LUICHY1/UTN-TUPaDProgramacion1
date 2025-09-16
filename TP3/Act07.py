#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
if numero >= 0:
    suma = 0
    for i in range(numero + 1): 
        suma += i
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")

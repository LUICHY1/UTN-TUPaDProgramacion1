#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
cantidad_numeros = 100
suma = 0
print(f"Ingresa {cantidad_numeros} números enteros:")
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))  
    suma += numero  
media = suma / cantidad_numeros
print(f"\nLa media de los números ingresados es: {media}")

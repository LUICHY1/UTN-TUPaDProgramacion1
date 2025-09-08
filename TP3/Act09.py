#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

def calcular_media():
    suma = 0
    cantidad = 100 
    print(f"Ingresa {cantidad} números enteros:")
    for i in range(1, cantidad + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
        suma += numero
    media = suma / cantidad
    print(f"\nLa media de los {cantidad} números ingresados es: {media:.2f}")
calcular_media()
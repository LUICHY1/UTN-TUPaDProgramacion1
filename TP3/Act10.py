#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

def invertir_digitos():
    while True:
        numero = input("Ingresa un número entero: ")
        if numero.lstrip('-').isdigit():
            numero_invertido = numero[::-1] if numero[0] != '-' else '-' + numero[:0:-1]
            print(f"El número invertido es: {numero_invertido}")
            break
        else:
            print("Entrada inválida. Por favor, ingresa un número entero.")
invertir_digitos()
def validar_entero_positivo(mensaje):

    entrada = input(mensaje)
    
    # Bucle: Se repite mientras la entrada NO sea un dígito
    # o si el número es 0 (queremos de 1 a 8)
    while not entrada.isdigit() or int(entrada) <= 0:
        print("Error: Debe ingresar un número entero positivo.")
        entrada = input(mensaje)
        
    # Si sale del bucle, es un número válido
    return int(entrada)

def validar_texto_no_vacio(mensaje):
    """
    Pide un texto al usuario hasta que ingrese algo (no vacío).
    """
    entrada = input(mensaje)
    
    # Bucle: Se repite mientras la entrada (sin espacios) esté vacía
    while entrada.strip() == "":
        print("Error: Este campo no puede estar vacío.")
        entrada = input(mensaje)
        
    return entrada.strip()
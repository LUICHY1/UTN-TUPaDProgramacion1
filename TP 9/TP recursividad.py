# Actividad 1)
#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num
    
def factorial_multiple(num):
    if num >= 1:
        print(factorial(num))
        factorial_multiple(num-1)
    
    
entrada = int(input("Dame un numero entero y te mostrare el factorial de todos los numeros entre el y 1: "))

factorial_multiple(entrada)


#Actividad 2)
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

def freno(limite, vuelta = 0):
    if vuelta > limite:
        return
    
    print(f"f fibonacci({vuelta}) = {fibonacci(vuelta)}" )

    freno(limite, vuelta + 1)
    
limite = int(input("Hasta que vuelta quieres que te muestre la serie de fibonacci: "))
freno(limite)

# Actividad 3)
#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente-1)

print("Vamos a calcular una potencia")
base = int(input("Decime la base: "))
exponente = int(input("Decime el exponente: "))

print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")


#Actividad 4)
#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto
import math


def pasaje_binario(num):
    if num == 0:
        return ""
    else:
        return pasaje_binario(num // 2) + str(num % 2)
    
numero = int(input("Dame un numero y lo convertire a binario: "))
print(pasaje_binario(numero))


#Actividad 5)
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es

def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            reduccion = palabra[1:-1]
            return es_palindromo(reduccion)
        else:
            return False
        
palabra = input("Dame una palabra y te dire si es un palindromo: ").strip().lower()
print(es_palindromo(palabra.replace(" ","")))


#Actividad 6)
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(num, acum = 0):
    if num == 0:
        return acum
    else:
        ultimo = num % 10
        actualizacion = num // 10
        acum += ultimo
        return suma_digitos(actualizacion, acum)

num = int(input("Dame un numero y sumare todos sus elementos: "))
print(suma_digitos(num))


#Actividad 7)
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide

def contar_bloques(bloques, acum = 0):
    if bloques == 1:
        return acum + 1
    else:
        acum += bloques
        bloques = bloques-1
        return contar_bloques(bloques, acum)

bloques = int(input("Dime cuantos bloques tienes en el ultimo nivel y te devolvere la cantidad necesaria para armar la piramide: "))
print(f"Necesitas {contar_bloques(bloques)} bloques")

#Actividad 8)
#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número

def contar_digito(numero, digito, acum = 0):
    if numero == 0:
        return acum
    else:
        item = numero % 10
        actualizacion = numero // 10
        if item == digito :
            acum += 1
            return contar_digito(actualizacion, digito, acum)
        else:
            return contar_digito(actualizacion, digito, acum)
        
print("Dame un numero y un digito y te dire cuantas veces aparece este en el numero")
numero = int(input("Dame el numero primero: "))
digito = int(input("Ahora dame el digito que deseas contar: "))

if 0<= digito <= 9:
    print(f"El numero {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
else:
    print("El digito tiene que estar entre 0 y 9")


#ACT1
#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num
    
def factorial_multiple(num):
    if num >= 1:
        print(factorial(num))
        factorial_multiple(num-1)
    
    
entrada = int(input("Dame un numero entero y te mostrare el factorial de todos los numeros entre el y 1: "))

factorial_multiple(entrada)

#ACT2
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

def freno(limite, vuelta = 0):
    if vuelta > limite:
        return
    
    print(f"f fibonacci({vuelta}) = {fibonacci(vuelta)}" )

    freno(limite, vuelta + 1)
    
limite = int(input("Hasta que vuelta quieres que te muestre la serie de fibonacci: "))
freno(limite)

#ACT 3
#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente-1)

print("Vamos a calcular una potencia")
base = int(input("Decime la base: "))
exponente = int(input("Decime el exponente: "))

print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

#ACT 4
#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto
import math


def pasaje_binario(num):
    if num == 0:
        return ""
    else:
        return pasaje_binario(num // 2) + str(num % 2)
    
numero = int(input("Dame un numero y lo convertire a binario: "))
print(pasaje_binario(numero))

#ACT 5
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es

def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            reduccion = palabra[1:-1]
            return es_palindromo(reduccion)
        else:
            return False
        
palabra = input("Dame una palabra y te dire si es un palindromo: ").strip().lower()
print(es_palindromo(palabra.replace(" ","")))

#ACT 6
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(num, acum = 0):
    if num == 0:
        return acum
    else:
        ultimo = num % 10
        actualizacion = num // 10
        acum += ultimo
        return suma_digitos(actualizacion, acum)

num = int(input("Dame un numero y sumare todos sus elementos: "))
print(suma_digitos(num))

#ACT 7
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide

def contar_bloques(bloques, acum = 0):
    if bloques == 1:
        return acum + 1
    else:
        acum += bloques
        bloques = bloques-1
        return contar_bloques(bloques, acum)

bloques = int(input("Dime cuantos bloques tienes en el ultimo nivel y te devolvere la cantidad necesaria para armar la piramide: "))
print(f"Necesitas {contar_bloques(bloques)} bloques")

#ACT 8
#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número

def contar_digito(numero, digito, acum = 0):
    if numero == 0:
        return acum
    else:
        item = numero % 10
        actualizacion = numero // 10
        if item == digito :
            acum += 1
            return contar_digito(actualizacion, digito, acum)
        else:
            return contar_digito(actualizacion, digito, acum)
        
print("Dame un numero y un digito y te dire cuantas veces aparece este en el numero")
numero = int(input("Dame el numero primero: "))
digito = int(input("Ahora dame el digito que deseas contar: "))

if 0<= digito <= 9:
    print(f"El numero {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
else:
    print("El digito tiene que estar entre 0 y 9")
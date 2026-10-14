"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:

- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def FizzBuzz():
    multiplo_3 = 3
    multiplo_5= 5
    
    for i in range(1,101):
        if i % multiplo_3 == 0 and i % multiplo_5 == 0:
            print("fizzbuzz")                 
        elif i % multiplo_3 == 0:
            print("fizz") 
        elif i % multiplo_5 == 0:
            print("buzz")
        else:
            print(i)


FizzBuzz()

"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) segun sean o no anagramas.

- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.

- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

"""

def isAnagrama(a: str, b: str):

    a = a.lower()
    b = b.lower()

    if a == b:
        return False
    
    return sorted(a) == sorted(b)

anagrama1 = isAnagrama("Amor","Roma")
print(anagrama1)

anagrama1 = isAnagrama("lol","Frase")
print(anagrama1)

# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13 ...
# f = (n-1) + (n-2)

def Fibonacci():
    a = 0
    b = 1
    for _ in range(50):
        print(a)
        a, b = b, a + b 
    

Fibonacci()

"""
¿ES UN NUMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(number)-> bool:
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def primos_1_100():
    for num in range(1, 101):
        if is_prime(num):
            print(num)


print(is_prime(5))

primos_1_100()

# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def area_poligono(tipo: str,valor1 = None,valor2 =None):

    if tipo == "triangulo":   
        return valor1 * valor2 / 2
    elif tipo == "cuadrado":
        return valor1 * valor1
    else:
        return valor1 * valor2

print(area_poligono("triangulo", 6, 4))
print(area_poligono("cuadrado", 5))
print(area_poligono("rectangulo", 8, 3))
    
# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invertir_cadena(cadena: str)-> str:
    invertida = cadena[::-1]
    return invertida

print(invertir_cadena("Hola python"))
print(invertir_cadena("Hola mundo"))

def invertir_cadena_manual(cadena: str)-> str:
    invertidad = ""

    for i in range(len(cadena) -1,-1,-1):
        invertidad += cadena[i]
    return invertidad


print(invertir_cadena("Hola python"))
print(invertir_cadena("Hola mundo"))

# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def decimal_binario(num):
    residuo = 0
    cociente = num
    binario = ""
    
    if num < 1:
        return 0
    
    while cociente >= 1:
        cociente,residuo = cociente // 2, cociente % 2
        binario = str(residuo) + binario

    return int(binario)

print(decimal_binario(13))

# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

def eliminar_caracteres(str1: str,str2: str)-> str:
    out1 = ""
    out2 = ""

    for caracter in range(len(str1)):
        if str1[caracter] not in str2:
            out1 += str1[caracter]
    
    for caracter in range(len(str2)):
        if str2[caracter] not in str1:
            out2 += str2[caracter]

    return out1,out2

    
print(eliminar_caracteres("la longitud de mi nombre","la circunferencia del circulo es"))

# /*
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */

def is_palindromo(str1):

    invertida = str1[::-1]
    str1_nueva = "".join(str1.split())
    invertida_nueva = "".join(invertida.split())

    return invertida_nueva.lower().split() == str1_nueva.lower().split()

print(is_palindromo("Ana lleva al oso la avellana"))
print(is_palindromo("Dábale arroz a la zorra el abad"))
print(is_palindromo("mundo"))



# /*
#  * Escribe una función que calcule y retorne el factorial de un número dado
#  * de forma recursiva.
#  */


# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# 15
# ¿ES UN NÚMERO DE ARMSTRONG?
# /*
#  * Escribe una función que calcule si un número dado es un número de Armstrong
#  * (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información
#  * al respecto.
#  */


def Armstrong(number):
    #cuando me dan un numero y quiero dividirlo en caracteres en una lista#
    digitos = [int(digito) for digito in str(number)]
    #cuando me dan un numero y quiero dividirlo en caracteres en una lista#
    acomulado = 0

    for index in range(len(digitos)):
        acomulado += digitos[index] ** len(digitos)

    if acomulado == number:
        return True, acomulado
    else:
        return False, acomulado

print(Armstrong(1634))



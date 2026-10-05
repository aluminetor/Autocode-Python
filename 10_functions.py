### Functions ###

# Declarar y llamar a una función
def comer (mordisco):
    print(mordisco)

comer("mordisco")

def generate_full_name ():
    first_name = 'pablo'
    last_name = 'jaramillo'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()



#Función que devuelve un valor - return
def generate_full_name ():
    first_name = 'pablo'
    last_name = 'jaramillo'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name ())

#Función con parámetros

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings("Pabo"))

#Función con parámetros predeterminados

def greetings (name = 'aluminetor'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('pabo'))

#Número arbitrario de argumentos

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

#Ejercicios: Día 11

#Ejercicios: Nivel 1
#Declara una función llamada add_two_numbers . Recibe dos parámetros y devuelve una suma.

def add_two_numbers(primer_valor, segundo_valor):
    print(primer_valor + segundo_valor)

add_two_numbers(2,2)

#El área de un círculo se calcula de la siguiente manera: área = π xrx r. Escribe una función que calcule el área_de_un_círculo .


def área_de_un_círculo (radio):
    return 3.1416 * (radio ** 2)

print(área_de_un_círculo(3))

"""
Escribe una función llamada `add_all_nums` que reciba un número arbitrario de argumentos y 
los sume todos. Verifica si todos los elementos de la lista son de tipo numérico. Si no lo son,
proporciona una retroalimentación adecuada.
"""


def add_all_nums (*nums):
    suma = 0
    for num in nums:
        if type(num) not in (int, float):
            return f"Error: El argumento '{num}' no es numérico."
        
        suma +=num
    return suma



print(add_all_nums(2,4))
print(add_all_nums(2, "4", 5))

#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit .


def convert_celsius_to_fahrenheit(celsius):
    
    fahrenheit = celsius * (9/5) + 32

    return fahrenheit 

print(convert_celsius_to_fahrenheit(4))


#Escribe una función llamada check-season, que reciba como parámetro el mes y devuelva la estación del año: otoño, invierno, primavera o verano.

otoño = ["octubre","noviembre","septiembre"]
invierno = ["enero","febrero","marzo"]
verano = ["julio","agosto","junio"]

def check_season (mes):
    if mes.lower() in otoño:
        estado = "otoño"
    elif mes.lower() in invierno:
        estado =  "invierno"
    else:
        estado = "verano"
    return estado

print(check_season("julio"))

#----------------forma mejor------------------

def check_season(mes):
    mes_limpio = mes.lower() .strip()

    estaciones = {
        "invierno":["enero","febrero","marzo"],
        "verano":["julio","agosto","junio"],
        "otoño":["octubre","noviembre","septiembre"],
        "primavera":["abril", "mayo"]
    }

    for estacion, meses in estaciones.items():
       if mes_limpio in meses:
            return estacion


    return "Mes no permitido"


print(check_season("julio"))      # verano
print(check_season("  ABRIL "))   # primavera
print(check_season("octubre"))    # otoño
print(check_season("enero"))      # invierno
print(check_season("manzana"))

#----------------forma mejor------------------

"""
La ecuación cuadrática se calcula de la siguiente manera
: ax² + bx + c = 0. Escribe una función que calcule el conjunto 
solución de una ecuación cuadrática, solve_quadratic_eqn .
"""

import math

def solve_quadratic_eqn(a, b, c):
    # Caso especial: Si a es 0, no es una ecuación cuadrática
    if a == 0:
        if b != 0:
            return -c / b  # Ecuación lineal: bx + c = 0
        return "Indeterminada o sin solución" if c == 0 else "Sin solución"
    
    # Cálculo del discriminante
    discriminante = b**2 - 4 * a * c
    
    if discriminante > 0:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        return (x1, x2)
    elif discriminante == 0:
        x = -b / (2 * a)
        return x
    else:
        return "No tiene soluciones reales"


# Pruebas:
print(solve_quadratic_eqn(1, -3, 2))   # Dos soluciones reales: (2.0, 1.0) -> x² - 3x + 2 = 0
print(solve_quadratic_eqn(1, -2, 1))   # Una solución real: 1.0 -> (x - 1)² = 0
print(solve_quadratic_eqn(1, 0, 1))    # Sin solución real: x² + 1 = 0
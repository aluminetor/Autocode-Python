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



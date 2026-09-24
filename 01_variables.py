# variables

my_name = "juanpablo"
my_lastname = "sanchezjaramillo"

full_name = "juanpablosanchezjaramillo"

print("palabra por palabra: ", list(my_lastname))
esta_solo = True
print(type(esta_solo))

nombre , hola = 'nombre' , 'hola'

print(nombre, hola)

print(len(full_name))

print("la longitud de mi nombre ", len(my_name), " y la de mi apellido ", len(my_lastname))




"""

El radio de un círculo es de 30 metros.
Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle.
Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle.
Toma el radio como entrada del usuario y calcula el área.

"""
import math
radio = 30
area_of_circle = math.pi * (radio ** 2) 
print("el area de un circulo con radio 30 es: ",area_of_circle)


circum_of_circle = 2 * math.pi * radio

print("la circunferencia del circulo es: ",circum_of_circle)

radio = int(input("dame el radio del circulo"))

area_of_circle = math.pi * (radio ** 2) 

print("el area de un circulo con radio", radio ,"es: ",area_of_circle)



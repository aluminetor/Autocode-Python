### conditionals ###

"""
 if , else y elif . 
 Los operadores lógicos y de comparación que aprendimos 
 en secciones anteriores serán útiles aquí.

"""

its_married = True

if its_married:
    print("esta casado")
else:
    print("no esta casado")


a = -1

if a > 0:
    print("numero positivo")
elif a == 0:
    print("es cero")
else:
    print("es negativo")

#Taquigrafía code if condition else code

print("A es positivo") if a > 0 else print("A es negativo")

#si anidado
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#operadores logicos

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')



#Ejercicios: Día 9

"""
Obtén la entrada del usuario usando input(“Ingresa tu edad: ”). 
Si el usuario tiene 18 años o más, dale el siguiente mensaje: 
Tienes edad suficiente para conducir. Si es menor de 18 años, 
dale el siguiente mensaje para que esperes a tener la cantidad de años 
que faltan. Salida:
"""
# UserAge = int(input("Ingresa tu edad..."))

# if UserAge >= 18:
#     print("Tienes edad suficiente para conducir")
# else:
#     print("No tienes la edad autorizada para conducir")

"""
Compara los valores de my_age y your_age usando if … else. 
¿Quién es mayor (yo o tú)? Usa input(“Ingresa tu edad: ”) para obtener la edad como entrada. 
Puedes usar una condición anidada para imprimir 'año' si la diferencia de edad es de 1 año, 'años' 
si la diferencia es mayor y un texto personalizado si my_age = your_age. Salida:
"""

# your_age = int(input("Ingresa tu edad..."))
# my_age = int(input("Ingresa mi edad..."))

# if my_age > your_age:
#     print("my_age es mayor")
# elif my_age == your_age:
#     print("edades iguales")
# else:
#     print("your_age es mayor")


# diferenciaEdades = abs(int(your_age - my_age))

# if diferenciaEdades == 1:
#     print("año")
# elif diferenciaEdades > 1:
#     print("años")
# else:
#     print("menos de un año")


"""
Obtén dos números del usuario mediante una solicitud de entrada. 
Si a es mayor que b, devuelve a mayor que b; si a es menor que b, 
devuelve a menor que b; en caso contrario, 
a es igual a b. Salida:
"""

# a = int(input("Digita un numero"))
# b = int(input("Digita un numero"))

# if a > b:
#     print(f"{a} mayor que {b}")
# elif a < b:
#     print(f"{a} menor que {b}")
# else:
#     print(f"{a} es igual a {b}")
    
#Ejercicios: Nivel 2

"""
Escribe un código que califique a los estudiantes según sus puntuaciones:
"""

# nota = int(input("ingrese la nota"))

# if nota >= 90 and nota <= 100:
#     print("A")
#     if nota >= 80 and nota <= 89:
#         print("B")
#         if nota >= 70 and nota <= 79:
#             print("C")
#             if nota >= 60 and nota <= 69:
#                 print("D")
# else:
#     print("F")


"""
Obtén el mes ingresado por el usuario y luego verifica si la estación es otoño, 
invierno, primavera o verano. Si el usuario ingresa: septiembre, octubre o noviembre, 
la estación es otoño. Diciembre, enero o febrero, la estación es invierno. Marzo, abril o mayo, 
la estación es primavera. Junio, julio o agosto, la estación es verano.
"""


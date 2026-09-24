### Strings ###

first_name = "Pablo"
last_name = "Sanchez"
space = " "

full_name = first_name + space + last_name

print(full_name)


#formateo

vol1, vol2, vol3, vol4 = "niveles","Videojuego",12,"RPG"
años = 5
print("Hoy me descarge\nun {} tipo {} que es muy divertido\ncuenta con {} mazmorras\ny varios {}".format(vol2,vol4,vol3,vol1))

print(f"sus segundos vividos son: {años * 31536000}")
 
#Cadenas de Python como secuencias de caracteres

language = "aluminetor"

a, b, c, d, e, f, g, h, i, j = language #guarda un caracter en cada variable

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)


print("Acceso a caracteres en cadenas mediante índice")

first_letter = language[-1]


print(first_letter)

#la última letra de una cadena está a la longitud de la cadena menos uno

last_index = len(language) - 1
last_letter = language[last_index]
print("ultima letra ", last_letter)

#Segmentación de cadenas de Python
print("Segmentación de cadenas de Python")

first_three = language[0:5] 
print(first_three)
last_three = language[5:10]
print(last_three)

last_three = language[-5:]
print(last_three)  
last_three = language[8:]
print(last_three)

#invertir 

frase = "viva Cristo Rey"

print(frase[::-1])

aui = language[0:6:2] 

print("aluminetor", aui)

print(language.capitalize())
print(language.lower())
print(language.upper())
print(language.count("t")) # cuenta cuantas "t" hay en "aluminetor"

challenge = 'thirty days of python'
print(challenge.title())

"""

Ejercicios - Día 4

"""

thirty, days, of, python = "thirty", "days", "of", "python"


Oracion_Completa =thirty+space+days+space+of+space+python

print(Oracion_Completa.title())

company = "Coding For All"

print(company,"\nLa Longitud es:",len(company))

print(company.upper())

print(company.lower())

print(company.lower(), company.title())

recortar = company[7:]

print(recortar)

print("Coding" in company)

#replace(): Reemplaza una subcadena con una cadena dada.

print(company.replace("Coding","Python"))

redes = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(company.split())

print(redes.split())

print(company[0])

print(len(company) - 1, company[len(company) - 1])

print(company.count("C"))
print(company.count("F"))

frase_2 = "Coding For All"

print(frase_2.rfind("l"))

frase_23 = "No se puede terminar una oración con because porque because es una conjunción"

print(frase_23.index("because"))

# ejercicio 25

frase_25 = "No puedes terminar una oracion con porque porque porque es una conjunción"

print(frase_25.replace(" porque porque porque",""))

#ejercicio 26

frase = "No puedes terminar una oración con because porque because es una conjunción"
print(frase.find("because"))

#¿'Coding For All' comienza con la subcadena Coding ?
# frase_2 = "Coding For All"

print(frase_2.startswith("Coding"))

#¿"Coding For All" termina con una subcadena "coding" ?

print(frase_2.endswith("coding"))


"""
' Codificación para todos ', 
elimina los espacios finales izquierdo y derecho en la cadena dada.

"""

Code_For_All = " Codificación para todos "

#La funcion .strip() verifica y elimina los caracteres de los extremos

print(Code_For_All.strip(" "))

thirty_days_python = "30 días de Python"

treinta_dias_python = "treinta_días_de_python"

print(thirty_days_python.isidentifier(), treinta_dias_python.isidentifier())

#La siguiente lista contiene los nombres de algunas bibliotecas de Python:

bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(", ".join(bibliotecas_python))

print("I am\nenjoying this challenge.")

print("name\tage\tcontry\tcity")

print(f"Asabene\t{250}\tFinland\tHelsinki")

a = 8

b = 6

print("{} + {} = {} " .format(a, b, a + b))

print("{} - {} = {} " .format(a, b, a - b))

print("{} * {} = {} " .format(a, b, a * b))

print("{} / {} = {} " .format(a, b, a / b))

print("{} % {} = {} " .format(a, b, a % b))

print("{} // {} = {} " .format(a, b, a // b))

print("{} ** {} = {} " .format(a, b, a ** b))




## loops ##
"""
Existen dos tipos
- bucle while
- bucle for
"""

""" BUCLE WHILE """
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

print("break")
#Break: Usamos break cuando queremos salir o detener el bucle.

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

print("continuar")

#Continuar: Con la instrucción continue podemos saltarnos la iteración actual y continuar con la siguiente:
count = 0
while count < 5:
    if count == 0:
        count += 1
        continue
    print(count)
    count = count + 1

""" BUCLE FOR """

#Un bucle se utiliza para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena de caracteres).

print("Bucle FOR")

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

for fruit in fruits:
    print(fruit)

#en una cadena

treinta_dias_python = "treinta_días_de_python"

for letter in treinta_dias_python:
    print(letter)


for i in range(len(treinta_dias_python)):
    print(treinta_dias_python[i])


#en una tupla
numbers = (0, 1, 2, 3, 4, 5)

for number in numbers:
    print(number)

numeral=0
for i in range(len(numbers)):
    print(f"posicion {numeral} numeral {numbers[i]}")
    numeral += 1

#Bucle for con diccionario. Recorrer un diccionario te da la clave del diccionario.
 

videojuego = {

    "titulo": "The Legend of Zelda: Breath of the Wild",
    "genero": "Acción-aventura",
    "plataformas": ["Nintendo Switch", "Wii U"],
    "año_lanzamiento": 2017,
    "puntuacion": 9.7,
    "completado": True

}

for clave in videojuego:
    print(clave)
    if clave == "genero":
        continue
    print("lol")
else:
    print("chaoo")



for clave, value in videojuego.items():
    print(clave, value)



#conjunto

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for companie in it_companies:
    print(companie)
    if companie == "IBM":
        print(f"no permitidad")


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


#La función de range(start, end, step)

lista = list(range(0,11,1))
print(lista)



## Ejercicios: Día 10

# Ejercicios: Nivel 1

#Itera del 0 al 10 usando un bucle for, haz lo mismo usando un bucle while.

for num in range(11):
    print(num)

#Itera del 10 al 0 usando un bucle for, haz lo mismo usando un bucle while.

for num in range(10,0,-1):
    print(num)


#Escribe un bucle que realice siete llamadas a print(), de manera que en la salida obtengamos el siguiente triángulo:

numeral = "#"

for num in range(7):
    print(numeral)
    numeral += "#"

#Utilice bucles anidados para crear lo siguiente:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #



for i in range(8):        
    for j in range(8):
        print("#", end = " ")
    print()


#Imprime el siguiente patrón:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

   
for i in range(11):
    print(f"{i} x {i} = {i*i}")


#Recorre la lista ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprime los elementos.

Python = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']


for pilares in Python:
    print(pilares)


#Utilice un bucle for para iterar de 0 a 100 e imprimir solo números pares.

for i in range(101):
    if i % 2 == 0:
        print(i)

#Utilice un bucle for para iterar de 0 a 100 e imprimir solo números impares.

for i in range(101):
    if i % 2 != 0:
        print(i)


#Ejercicios: Nivel 2

#Utilice un bucle for para iterar desde 0 hasta 100 e imprimir la suma de todos los números.

sumaall = 0

for i in range(101):
    sumaall += i

print("The sum of all numbers is", sumaall)

pares = 0
for i in range(101):
    if i % 2 == 0:
        pares +=i

impares = 0
for i in range(101):
    if i % 2 != 0:
        impares +=i

print("The sum of all pares is", pares ,"And the sum of all impares is", impares)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for pais in countries:
    if "land" in pais.lower():
        print(pais)

#Esta es una lista de frutas, ['plátano', 'naranja', 'mango', 'limón'] invierta el orden usando un bucle.

fruits = ['plátano', 'naranja', 'mango', 'limón']

fruitsinvert = []


i = len(fruits) -1 

while i >= 0:
    fruitsinvert.append(fruits[i])
    i -=1 

print(fruitsinvert)


fruits = ['plátano', 'naranja', 'mango', 'limón']

fruitsinvert = []

for i in range(len(fruits) - 1, -1, -1):
    fruitsinvert.append(fruits[i])

print(fruitsinvert)

# otra manera

fruits = ['plátano', 'naranja', 'mango', 'limón']
fruitsinvert = []

for fruit in reversed(fruits):
    fruitsinvert.append(fruit)

print(fruitsinvert)


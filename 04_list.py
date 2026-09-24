#Listas
#existen dos maneras: llamamos a la funcion list() o corchetes[]

lst = list()

fruits = ['banana', 'orange', 'mango', 'lemon',"1","2","3"]
print(len(fruits), fruits)

#diferentes tipos de datos dentro de una misma lista
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

print(lst)

Primer_Fruta = fruits[0]
print(Primer_Fruta)

Segunda_Fruta = fruits[1]
print(Segunda_Fruta)
#[0, 1, 2, 3, 4, 5] LA LONGITUD ES LEN() - 1

ultimo_index = len(fruits) - 1

ultima_fruta = fruits[ultimo_index]

print(ultima_fruta)

print("Desempaquetado de los artículos de la lista")

primeraF , segundaF, tercerF, cuartaF, *rest = fruits

#*rest muestra lo sobrante en forma de lista

print(primeraF)
print(segundaF)
print(tercerF)
print(cuartaF)
print(rest)

"""

Indexación positiva: Podemos especificar un 
rango de índices positivos indicando el inicio, 
el final y el paso; el resultado será una nueva lista. 
(Valores predeterminados: inicio = 0, final = longitud(último elemento) - 1, paso = 1)

"""
print("Segmentar elementos de una lista")


frutas = ["banana", "orange", "mango", "lemon"]
inicio, final, paso = 0, int(len(frutas) - 1) , 1

todasFrutas = frutas[0:4]

print(frutas[1:2:1])

print("ANALIZAR")
#lista = [inicio: fin: paso]
"""
inicio (primer argumento): Desde qué posición (índice) empieza a contar.

fin (segundo argumento): En qué posición se detiene (sin incluir ese elemento).

paso (tercer argumento): De cuánto en cuánto avanza. Por defecto es 1 (va elemento por elemento).
"""

print(frutas[::-1])

print(frutas[-3:-1])

print("Modificar listas")

adios = ["estres", "ansiedad", "temor", "ira"]

adios[0] = "relax"
adios[1] = "tranquilidad"
adios[2] = "valor"
adios[3] = "calma"

print(adios)

print("relax" in adios)

#insetar elementos en una lista

lst = list()

lst.append("PC")

print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append("melocoton")

fruits.append("manzana")

print(fruits, "manzana" in fruits)

lst = ["item1", "item2"]
lst.insert(0, "portatil")
print(lst)

print("quitar elementos de la lista: item1")

lst.remove("item1")

print(lst)
#El método pop() elimina el índice especificado (o el último si no se especifica)

fruits.pop(3) #elimina ["lemon"]
print(fruits)

#eliminar utilizando del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0]
print(fruits)



#Borrar elementos de la lista. El método clear() vacía la lista:

fruits.clear()

print(fruits)

#Funcion COPIAR una lista a otra

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_copy = fruits.copy()

print(fruits_copy)

#union de listas
union_plus = lst + fruits_copy
print(union_plus)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]

list1.extend(list2)

print(list1)

print("Funcion count en listas: cuantas veces aparece")

mi_lista = ['a', 'b', 'a', 'c', 'a']

print(mi_lista.count("a"))

print("el indice de un elemento dentro de la lista")

print(fruits.index("orange"))

invertida = ["aloH", "Hola"]

invertida.reverse()

print(invertida)

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.sort()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

# Ejercicios: Día 5

eternals = ['Sersi', 'Ikaris', 'Ajak', 'Kingo', 'Thena', 'Phastos', 'Makkari', 'Druig', 'Gilgamesh', 'Sprite']
print(len(eternals),"Mitad ", len(eternals) // 2)
print("primer ",eternals[0],"medio ",eternals[len(eternals) // 2],"segundo",eternals[-1])

mixed_data_types = ["Pablo", 19, 1.80, "Soltero", "3150 South Delaware Street, San Mateo, CA 94403, Estados Unidos"]

compañias = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(compañias)

print(len(compañias))

print("1er", compañias[0], "mid", compañias[len(compañias) // 2],"Ultima", compañias[-1])

#Imprime la lista después de modificar una de las empresas.

#1er forma
compañias[1] = "Instagram"
print(compañias)

#Agregar una empresa de TI a it_companies

compañias.append("AWS")

print(compañias)

#Inserta una empresa de TI en medio de la lista de empresas.

compañias.insert(len(compañias) // 2, "Roblox")
print(compañias)

#Cambia uno de los nombres de las empresas de TI a mayúscula

print("#Cambia uno de los nombres de las empresas de TI a mayúscula")
indice = 2

if compañias[indice] != "IBM":
    compañias[indice] =compañias[indice].upper()

print(compañias)

#Une las empresas de TI con una cadena '#;'

print("#;".join(compañias))

#Comprueba si una empresa determinada existe en la lista it_companies.

print("IBM" in compañias)
print(compañias.count("IBM") > 0)
print(compañias.index("IBM"))
#Ordena la lista usando el método sort().

compañias.sort()

print(compañias)

#nvierte la lista en orden descendente usando el método reverse().

compañias_invertida = compañias.copy()

compañias_invertida.reverse()

print(compañias_invertida)

#Elimina las tres primeras empresas de la lista.
print("sin eliminar: ",compañias)
del compañias[0:3]
print(compañias)

#Elimina las últimas 3 empresas de la lista.
print("sin eliminar: ",compañias)
del compañias[-3:]
print(compañias)

#Elimine de la lista la empresa o empresas de TI intermedias.
compañias = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("sin eliminar: ",compañias)
del compañias[len(compañias) // 2]
print(compañias)


compañias.pop(0) #elimina la primera empresa
print(compañias)

compañias = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("sin eliminar: ",compañias)
del compañias[0::2]
print(compañias)

compañias = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
compañias.pop()
print(compañias)

compañias.clear()
print(compañias)

#union de listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

nueva_lista = front_end.__add__(back_end)

print(nueva_lista)

full_stack = front_end + back_end
print(full_stack)
indice = 4
full_stack.append("Python")
full_stack.insert(indice + 1,"SQL")

print(full_stack)


#Ejercicios: Nivel 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Ordena la lista y encuentra la edad mínima y máxima.

ages.sort()

print(ages)

edad_min = ages[0]

edad_max = ages[-1]

print("Edad min:", edad_min ,"Edad max:", edad_max)

#Calcula la mediana de edad (un valor central o dos valores centrales divididos entre dos)

ages.sort()

edad_mediana = ages[len(ages) // 2]

print("Mediana", edad_mediana, ages)

#promedio
ages = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

print(ages)

suma_ages = 0

for i in range(len(ages)):
    suma_ages = ages[i] + suma_ages

print("Suma de todos: ",suma_ages)

promedio = suma_ages / len(ages)

print("y su promedio: ",promedio)

#-------------------OTRA MANERA--------------------------------
print("OTRA MANERA")
suma_ages = 0
for age in ages:
    suma_ages += age
print("Suma de todos: ",suma_ages)

#RANGO

rango = edad_max - edad_min

print("rango: ",rango)

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


print("El pais del medio es",countries[len(countries) // 2])

#Divide la lista de países en dos listas iguales si es par; de lo contrario, agrega un país más para la primera mitad.
countries.insert(len(countries) // 2,"robloxia")

dv1= []

for i in range(0, len(countries) // 2):
    dv1.insert(i,countries[i])

print(len(countries))
print(len(dv1),dv1)
       
dv2 = []
for i in range(len(countries) // 2,len(countries)):
    dv2.insert(i,countries[i])

print(len(countries))
print(len(dv2), dv2)

mini_lista = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

primeros = mini_lista[0:3]

resto = mini_lista[3:len(mini_lista)]

print(primeros, resto)
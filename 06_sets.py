##sets## => conjunto

#conjunto vacio

st = {"Hola", "Como", "Va", "Todo"}

print(type(st))

print("Exite va? ", "Va" in st)

fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.add("Fresa") # No podemos modificar ningún elemento, pero sí podemos añadir elementos adicionales

fruits.update(["cebolla", "papa", "manzana"])

#eliminar elementos

fruits.remove("orange")

#elimina un elemento aleatorio 
remove_item = fruits.pop()

print(fruits, "fruta borrada", remove_item)

#---------Eliminar toda la lista--------------
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
#Eliminar un conjunto
biblicos = {"Genesis", "Levitico", "Probervios", "Salmos"}
del biblicos
#---------------------------------------------

#---------Lista a conjunto--------------

eternals = ['Sersi', 'Ikaris', 'Ajak', 'Kingo', 'Thena', 'Phastos', 'Makkari', 'Druig', 'Gilgamesh', 'Sprite']

lista_convert = set(eternals)

print(lista_convert)

avengers = {"Steve", "Tony", "Thor", "Bruce", "Natasha", "Clint"}

eternals_avengers = lista_convert.union(avengers)

#---------------------------------------------
#Encontrar elementos de intersección

avengers.intersection(eternals_avengers)

print(avengers.intersection(eternals_avengers))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

#---------------------------------------------

#---------Diferencia entre conjuntos--------------

print(whole_numbers.difference(even_numbers))
print(even_numbers.difference(whole_numbers))

#---------------------------------------------


#---------Ejercicios: Día 7--------------

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Ejercicios: Nivel 1

#Encuentra la longitud del conjunto it_companies

print(len(it_companies))

#Agregar 'Twitter' a it_companies

it_companies.add("Twitter")

print(it_companies)

#Inserta varias empresas de TI a la vez en el conjunto it_companies.

it_companies.update(["NVIDIA", "AMD", "Intel", "TSMC"])

print(it_companies)

#Eliminar una de las empresas del conjunto it_companies.

it_companies.remove("Apple")
print(it_companies)

#Ejercicios: Nivel 2

#Une A y B

c = A.union(B)

print(c)

#Encuentra la intersección A con B

print(f"A {A} y B {B}, intersección", A.intersection(B))


#¿Es A un subconjunto de B?

print(A.issubset(B))

#¿Son A y B conjuntos disjuntos?

print(A.isdisjoint(B))

unionAB = A.union(B) 
unionBA = B.union(A)

print(f"union A con B {unionAB} y union B con A {unionBA}")

#Ejercicios: Nivel 3

#Convierte las edades en un conjunto y compara la longitud de la lista y del conjunto, ¿cuál es mayor?

AgeSet = set(age)

print(f"la longitud de la lista {len(age)}, la del conjunto {len(AgeSet)}")

#Explica la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
"""
Cadena es un dato delimitado por comillas
lista es un grupo de datos que se pueden repetir y modificar
una tupla es un grupo de datos no inmutable
y un conjunto es un grupo de datos unicos
"""

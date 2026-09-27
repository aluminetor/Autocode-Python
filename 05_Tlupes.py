#tuples

"""
Una tupla es una colección de diferentes tipos de datos, ordenada e inmutable. 
Las tuplas se escriben entre paréntesis, (). Una vez creada una tupla, 
no se pueden modificar sus valores. No se pueden usar los métodos add, 
insert ni remove en una tupla porque no es modificable (mutable).

"""



#Ejercicio: nivel 1


my_cousins = ("Juan", "Duvan", "Johan", "Cristian")

my_aunts = ("Rosa", "Amparo", "Doralba", "Mary")


union_truple = my_cousins + my_aunts

print(union_truple, len(union_truple))

print(type(union_truple))
#Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members.

union_truple = list(union_truple) #para poder modificar y agregar

print(type(union_truple))

union_truple.insert(0, "Isabel")
union_truple.insert(1, "Euclides")

union_truple = tuple(union_truple) #Vuelve a ser tuple

print(type(union_truple))


family_members = union_truple

print(family_members, type(family_members))

#Ejercicios: Nivel 2

frutas = ("Sandia", "Fresa", "Manzana")
verduras = ("Cebolla", "Tomate", "Berenjena")
product_animal = ("Pescado", "Pollo", "Huevo")

union = frutas + verduras + product_animal

print(union)

union = list(union)
print(type(union))

union.insert(0, "food_stuff_tp")

union = tuple(union)
print(type(union), union, len(union))

#extraer

print(union[len(union) // 2])

union = list(union)


print(union)

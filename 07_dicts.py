### Dictionaries ###

my_other_dict = dict()
my_dict = {
    "first_name":"Pablo", 
    "last_name":"Sanchez", 
    "age":250,
    "country":"Robloxia",
    "is_marred":False,
    "skills":['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}

print(len(my_dict))

#Acceso a los elementos del diccionario

print(my_dict["first_name"])
print(my_dict["last_name"])
print(my_dict["skills"])

#Agregar elementos a un diccionario

my_dict["games"] = "Roblox"
my_dict["Anime"] = ["One piece"]
my_dict["Anime"].append("solo leveling")

print(my_dict)



#Modificación de elementos en un diccionario


videojuego = {

    "titulo": "The Legend of Zelda: Breath of the Wild",
    "genero": "Acción-aventura",
    "plataformas": ["Nintendo Switch", "Wii U"],
    "año_lanzamiento": 2017,
    "puntuacion": 9.7,
    "completado": True

}

videojuego["puntuacion"] = 9.8

print(videojuego)

#Comprobación de claves en un diccionario

print("titulo" in videojuego)

#Eliminar pares clave-valor de un diccionario.

del videojuego["completado"]
print(videojuego)


#El método items() convierte un diccionario en una lista de tuplas.
print(videojuego.items())

#Limpiar un diccionario 

#Obtener las claves del diccionario como una lista

games = videojuego.keys()
print(games)

#Obtener valores de diccionario como una lista

values = videojuego.values()
print(values)


#------------Ejercicios: Día 8------------

perro = dict()

perro=  {
    "nombre":"grogi", 
    "color":"atigrado",
    "raza":"galgo",
    "patas":4,
    "edad":3,
}

estudiantes = {
    "first_name":["Lucas","Ana"],
    "last_name":["Chaverra","Nandez"],
    "age":[18,19],
    "is_marred":[False,False],
    "skills":["Correr","Bailar"],
    "country":["Colombia","Brasil"],
    "city":["Medellin","Rio de janeiro"],
    "address ":["cra 37 bb51","cll 54# 35"],

}

print(len(estudiantes))

print(estudiantes["skills"], type(estudiantes["skills"]))

#Modifica los valores de las habilidades añadiendo una o dos habilidades.

print("añadiendo una o dos habilidades")

estudiantes["skills"].append("Nadar")
estudiantes["skills"].append("Leer")

print(estudiantes)

#Obtener las claves del diccionario como una lista

print(estudiantes.keys())

#Obtener valores de diccionario como una lista

print(estudiantes.values())

#Convierta el diccionario en una lista de tuplas usando el método items().
del estudiantes["address "]
print(estudiantes)

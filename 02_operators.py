# Operadores

print(3 >= 4)
print("buee " * (2 ** 2))

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density

print(len("pablo") < len("sanchez"))

print('z' not in 'lamparaesamispiez')

texto_origin = 'MODEL'
texto_min = texto_origin.lower()

print('model' is texto_min)

#Ejercicio - Dia 3

my_age = int(19)

my_height = 1.80

num_complejo = 1 + 2j

base_triangle = float (input("Ingrese la base"))

height_triangle = float (input("Ingrese la altura"))

area_of_triangle = base_triangle * height_triangle / 2

print("El area del triangulo es ", area_of_triangle)

lado_a = int(input("Ingrese lado a"))
lado_b = int(input("Ingrese lado b"))
lado_c = int(input("Ingrese lado c"))

perimetro = lado_a + lado_b + lado_c

print("el perimetro del triangulo es:", perimetro)


x = 2

y = 2 * x - 2

mp = (x / y) * 100

print("La pendiente de la recta" + "es", y )



x1 = 2 
x2 = 6
y1 = 2
y2 = 10

m = (y2 - y1) / (x2 - x1)

d = ((x2-x1) ** 2 + ((y2 - y1) ** 2)) ** (1/2)

print("La m de la recta", m , "la distancia euclidiana: ", d)



print(not(len("Python") is len("Dragon")))

print("on" in "Python" and "on" in "Dragon")

print("jerga" in "Espero que este curso no esté lleno de jerga")

print(("on" not in "piton" and "on" not in "Dragon"))

print(int(9.8) == 10)



años = int(input("Ingrese sus años vividos: "))

print(f"sus segundos vividos son: {años * 31536000}")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)




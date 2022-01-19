# 1. TAREA: imprimir "Hola mundo"
print("hola mundo")

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hola ", name)	# con una coma
print("Hola " + name)	# con un +

# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print("Hola", name)	# con una coma
print("Hola " + str(name))	# con un + - !Este debería darnos un error!

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} y {}".format(fave_food1,fave_food2)) # con .format()
print(f"Me encanta comer {fave_food2} y {fave_food1}") # con una cadena f

#5. Almacena tu nombre en una variable y luego úsalo para imprimir la cadena "¡Hola {{tu nombre}}!" usando una coma en la función de impresión (# 2a)
name = "Sebastian"
print("!Hola",name)
print("!Hola "+ name)

#6 . Almacena tu número favorito en una variable, y luego úsalo para imprimir la cadena "¡Hola {{num}}!" usando una coma en la función de impresión (# 3a)

num = 14
print("!hola",num)
print("!Hola " + str(num))

#7. Almacena 2 de tus comidas favoritas en variables y luego úsalas para imprimir la cadena "Me encanta comer {{food_one}} y {{food_two}}". con el método de formato (# 4a)
food_one = "lasagna"
food_two = "sushi"
print("Me encanta comer {} y {}".format(food_one,food_two))
print(f"Me encanta comer {food_one} y {food_two}")



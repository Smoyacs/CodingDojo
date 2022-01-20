
import random

def randInt(min=0, max=100):
    num = (random.random() * max) + min
    if min > max:
        print("El minimo debe ser menor que el maximo")
        return False

    elif num > max:
        num = max
        return round(num)
    
    elif max < 0:
        print("El valor maximo debe ser mayor a 0")
        return False

    else:
        return round(num)
print(randInt()) 		# debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50)) 	# debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	# debería imprimir un número aleatorio entre 50 a 100copy
print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 
print(randInt(min=-500, max=-200))    # debería imprimir un número aleatorio entre 50 y 
print(randInt(100,70))



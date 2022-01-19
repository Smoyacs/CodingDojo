#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

def cuenta_regresiva(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    print(arr)

cuenta_regresiva(5)

# Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([1,2])

# First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def first_plus_length(list):
    print(f"El primer valor es {list[0]} y su longitud es {len(list)}")
    print(list[0] + len(list))

first_plus_length([1,2,3,4,5])

# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

def values_greater_than_second(list):
    list2 = []
    if len(list)<2:
        return False
    
    else:
        for i in range(len(list)):
            if list[i] > list[1]:
                list2.append(list[i])
        print(len(list2))
        print(list2)        

values_greater_than_second([5,2,3,2,1,4,5,7,10,1])

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

values = []
def length_and_value(x,y):
    for i in range(x):
        values.append(y)
    print(values)

length_and_value(6,2)

# #1. Basico imprime todos los enteros del 0 al 150.
# for i in range(151):
#     print(i)

# #2. multiplos de 5 imprime todos los múltiplos de 5 de 5 a 1,000

# for i in range(0,1001,5):
#     print(i)

# #3. Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".

# for i in range(1,101,1):
#     if i%10 == 0 and i%5 == 0 :
#         print("Coding Dojo")
#         continue
#     elif i%5 == 0 :
#         print("Coding")
#         continue
    
#     print(i)


# #4. ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
# sum = 0
# for i in range(0,500001):
#     if i%2 != 0:
#         sum = sum + i

# print(sum)

# #5. Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
# for i in range(2018,0,-4):
#     print(i)
#     if i == 2:
#         print(0)

# #6. Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

# def contador(lowNum,highNum,mult):
#     for i in range(lowNum,highNum+1):
#         if i%mult == 0:
#             print(i)

# contador(2,9,3)

# Bonus

def isPrime(num):
    if num > 1:
        for j in range(1, num+1):
            if j == 2:
                print(f"{j} Es un numero primo")
            elif j == 3:
                print(f"{j} Es un numero primo")   
            elif j == 7:
                print(f"{j} Es un numero primo")        
            elif j%2 == 0 or j%3 == 0 or j%5 == 0 or j%7 == 0:
                continue
            else:
                print(f"{j} Es un numero primo")

isPrime(100)
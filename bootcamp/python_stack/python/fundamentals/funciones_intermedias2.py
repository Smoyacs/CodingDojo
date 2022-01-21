# #1. Actualiza los valores en some_dicts y listas
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
# x[1][0] = 15
# print(x)
# # Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
# students[0]["last_name"] = 'Bryant'
# print(students)
# # En el directorio sports_directory, cambia 'Messi' a 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# # Camba el valor 20 en z a 30
# z[0]['y'] = 30
# print(z)


#2. Itera a través de una lista de some_dicts
# Crea una función iterateDictionary(some_list)que, dada una lista de some_dicts, la función recorra cada some_dict de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print('first_name - '+students[i]["first_name"] + ', last_name - ' +students[i]["last_name"])
iterateDictionary(students)
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordans
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3. Obtén valores de una lista de some_dicts
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de some_dicts y un nombre de clave, la función imprima el valor almacenado en esa clave para cada some_dict. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('last_name', students)

#4.Itera a través de un some_dict con valores de listas
# Crea una función printInfo(some_dict)que, dado un some_dict cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
print("\n")
def printInfo(some_dict):
    for i in some_dict:
        # header
        print(len(some_dict[i]),i)
        # content
        for j in range(len(some_dict[i])):
            print(some_dict[i][j])
        print("")

printInfo(dojo)
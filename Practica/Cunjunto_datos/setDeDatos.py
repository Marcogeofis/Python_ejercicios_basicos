"""Set de datos

Los set de datos son una colección de elementos únicos e inmutables.

Algunos ejemplos sencillos:
"""

my_set1 = { 3, 4, 5}
print("My set = ", my_set1)

my_set2 = { "Hola", 23.3, False, True}
print("My set 2 = ", my_set2)

my_set3 = { 3, 3, 5}
print("My set 3 = ", my_set3)

# Los array y diccionarios son mutables y los set son inmutables por eso marca error
#my_set4 = { [1, 2, 3], 4}
#print("My set 4 = ", my_set4)
empty_set = {}
empty_set1 = type(empty_set)

empty_set = set()
empty_set2 = type(empty_set)
print("PAra identificar un set de un dict usamos type()")
print(f"Por ejemplo empty_set_dict = {empty_set1}, empty_set = {empty_set2} ")

# llamando tuplas
print('*'*36)
print('llamando tuplas')
my_list = [1,1,2,3,4,5,4]
my_set5 = set(my_list)
print(my_set5)

print('*'*36)
my_tuple = ("Hola", "Hola", "Hola", 1)
my_set6 = set(my_tuple)
print(my_set6)
"""Operaciones con sets

Unions se usa para tomar los valores de un conjunto de datos A y un conjunto B.
Donde se mesclan para tener un nuevo conjunto de datos con la mescla de A y B.
"""

my_set1 = {3,4,6}
my_set2 = {5,6,7}

print('Con junto de set1: ', my_set1)
print('Con junto de set2: ', my_set2)

print('*'*60)
print('Aplicando "union" en el conjunto de datos.')
my_set3 = my_set1 | my_set2
print(my_set3)


print('='*60)
my_set4 = {1,2,5,3,6,78,9}
my_set5 = {9,5,4,6,87,2,1,3}

print('Con junto de set4: ', my_set4)
print('Con junto de set5: ', my_set5)

print('*'*60)
print('Aplicando "union" en el conjunto de datos.')
my_set6 = my_set4 | my_set5
print(my_set6)

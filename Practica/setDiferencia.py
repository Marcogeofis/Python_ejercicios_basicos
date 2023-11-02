"""Diferencia

Es una operación que se utiliza para encontrar los elementos que están en un conjunto A pero no en otro.
En otras palabras, te permite determinar qué elementos son exclusivos de un conjunto en comparación con 
otro.

"""

my_set1 = {3,4,5}
my_set2 = {5,6,7}

print('Con junto de set1: ', my_set1)
print('Con junto de set2: ', my_set2)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos set1 - set2.')
my_set3 = my_set1 - my_set2
print(my_set3)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos set2 - set1.')
my_set4 = my_set2 - my_set1
print(my_set4)

print('*'*60)
print('Como se puede ver la diferencia de los conjuntos no es isgual')
print('set1 - set2 = set2 - set1. No es conmutativa.')

print('='*60)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print('Con junto de A: ', A)
print('Con junto de B: ', B)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos A - B.')
C = A - B
print(C)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos B - A.')
C = B - A
print(C)

print('*'*60)
print('Como se puede ver la diferencia de los conjuntos no es isgual')
print('A - B = B - A. No es conmutativa.')
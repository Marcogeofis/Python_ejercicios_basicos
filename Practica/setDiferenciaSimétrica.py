""" Diferencia simétrica

Es una operación que devuelve los elementos que son exclusivos de cada conjunto,
es decir, los elementos que están en uno de los conjuntos pero no en ambos.
Es una forma de encontrar la unión de los elementos que no son compartidos entre los conjuntos.

"""

my_set1 = {3,4,5}
my_set2 = {5,6,7}

print('Con junto de set1: ', my_set1)
print('Con junto de set2: ', my_set2)

print('*'*60)
print('Aplicando "diferencia simétrica" en el conjunto de datos.')
my_set3 = my_set1 ^ my_set2
print(my_set3)

print('*'*60)
print('La diferencia simétrica de set1 ^ set2 contiene todos los elementos que están en set1 o en set2, pero no en ambos.')

print('='*60)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print('Con junto de A: ', A)
print('Con junto de B: ', B)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos A - B.')
C = A ^ B
print(C)

print('*'*60)
print('Aplicando "diferencia" en el conjunto de datos B - A.')
C = B ^ A
print(C)

print('*'*60)
print('Como se puede ver la diferencia de los conjuntos es isgual')
print('A - B = B - A. Si es conmutativa.')
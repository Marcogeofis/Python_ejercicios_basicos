""" Intersección

Se usa para tomar los valores de un conjunto de datos A y un conjunto de datos B. 
Donde los conjuntos de A puede que se encuentren algunos datos repetidos en el conjunto de datos B,
por lo tanto, el nuevo conjunto de datos C sólo contendra los datos de A y que se encuentren
repetidos en B.

"""

my_set1 = {3,4,6}
my_set2 = {5,6,7}

print('Con junto de set1: ', my_set1)
print('Con junto de set2: ', my_set2)

print('*'*60)
print('Aplicando "Intersection" en el conjunto de datos.')
my_set3 = my_set1 & my_set2
print(my_set3)
print('Sólo se extrae los datos que estan en el conjunto del set1 y que se encuentren repetidos en set2 como el 6 que está en los dos conjuntos')

print('='*60)
my_set4 = {1,2,5,3,6,78,9}
my_set5 = {9,5,4,6,87,2,1,3}

print('Con junto de set4: ', my_set4)
print('Con junto de set5: ', my_set5)

print('*'*60)
print('Aplicando "Intersection" en el conjunto de datos.')
my_set6 = my_set4 & my_set5
print(my_set6)


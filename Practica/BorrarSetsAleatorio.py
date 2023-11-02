"""
Borrar un set de forma aleatoria

pop()
clear()
"""


myset = {1,2,3,4,5,6,7}
print("Mi set: ", myset)

print('*'*30)
print('borro con pop() de forma aleatorio')
myset.pop()
print(myset)


print('*'*30)
print('borro todo con clear()')
myset.clear()
print(myset)

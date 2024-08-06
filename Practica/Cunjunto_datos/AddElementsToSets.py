"""
Métodos que agregan elmentos a un set

add()
update()

Métodos que quitar elmentos a un set

discar()
remove()

"""

myset = {1,2,3}
print("Mi set: ", myset)

myset.add(4)
print("Agrego el elemento 4 a mi set", myset)

print('*'*30)
print('puedo agregar una lista de elementos, pero si algunos elementos son repetidos no los ingresa')
myset.update([1,2,5])
print('Agrego esta lista de elementos [1,2,5]')
print(myset)


print('*'*30)
myset.update((1,7,2), {6,8})
print('Agrego una tupla [1,7,2] y un set {6,8}')
print(myset)


print('*'*30)
print('Borrar elementos con remove o discard')
myset.discard(1)
print('Borro el elemento 1 con discard(1)')
print(myset)

print('*'*30)
myset.remove(2)
print('Borro el elemento 2 con remove(2)')
print(myset)

print('*'*30)
myset.discard(10)
print('Borro el elemento 10 que no existe con discard(2)')
print(myset)

print('*'*30)
myset.remove(12)
print('Borro el elemento 10 que no existe con remove(12)')
print(myset)

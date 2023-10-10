"""
En este simple ejercicio se practica el uso de funciones de orden superior.

Caso 1.- Funciones que toman funciones como argumentos

Caso 2.- Funciones que devuelven funciones
"""

# Caso 1

def aplicar(func, li):
    resultado = []
    for elemento in li:
        resultado.append(func(elemento))
    return resultado

def cuadrado(x):
    return x**2

def multiplicador(n):
    def multiplicar(x):
        return x*n
    return multiplicar

if __name__ == '__main__':
    
    numeros = [1,2,3,4,5]
    resultado = aplicar(cuadrado, numeros)
    print('Lista que entra en la funcionde de orden superior.', numeros)
    print('Su resultado es.', resultado) # -> [1, 4, 9, 16, 25]
    print('\n')
    print('************************************************\n')
    duplicar = multiplicador(5)
    triplicar = multiplicador(3)
    print('Ya se asignaron las variables duplicar y triplicar, como funciones que devuelven funciones')
    print(duplicar(2))
    print(triplicar(9))
"""
Para encontrar un número primo es de la siguiente manera.

En lugar de verificar todos los números hasta n, solo necesitas verificar los números hasta la raíz cuadrada de n. Si n es divisible por cualquier número en este rango, entonces n no es primo. Si no es divisible por ninguno de estos números, entonces n es primo

"""

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def prime_in_range(start, end):
    primes = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == '__main__':
    start = 10
    end = 50
    
    print(prime_in_range(start, end))
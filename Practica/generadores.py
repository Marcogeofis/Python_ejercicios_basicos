"""Generadores
Son funciones que básicamente guardan un estado, pero para entender 
que los generadores son iteradores pero más simples y elegantes.

La palabra yield es igual a la palabra return, pero return termina
la función y yield solo pausa la función.

"""

def my_gen():
    print("Hellow world")
    n = 0
    yield n
    
    print("Hellow heaven")
    n = 1
    yield n
    
    print("Hellow hell")
    n = 2
    yield n
    
if __name__=='__main__':
    a = my_gen()
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
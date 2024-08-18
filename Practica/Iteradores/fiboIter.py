"""Iteradores

Es una estructura de datos para guardar datos infinitos.
Esto nos ahorra recursos, ocupan poca memoria, son paracidos a las imágenes svg.

volveremos a usar la serie de Fibonacci pero con el iterador.

No funciono el código verificar ¿por qué?
"""

class FiboIter():
    def __init__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        
if __name__ == '__main__':
    fibonacci = FiboIter()
    for el in fibonacci:
        print(el)

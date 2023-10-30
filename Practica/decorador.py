def decorador(func):
    def envoltura():
        print('Este se añade a mi función original.')
        func()
    return envoltura


def saludo():
    print('¡Hola!')

if __name__ == '__main__':
    saludo = decorador(saludo)
    saludo()
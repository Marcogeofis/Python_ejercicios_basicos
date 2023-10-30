"""El decorador como se vió en el ejercicio anterior
va a cambiar la forma de asignar la función con @NombreDeLaFunción.
A esto se le conoce como azúcar sintántica.
"""



def decorador(func):
    def envoltura():
        print('Este se añade a mi función original.')
        func()
    return envoltura

@decorador
def saludo():
    print('¡Hola!')

if __name__ == '__main__':
    saludo()
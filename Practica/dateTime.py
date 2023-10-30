from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        inital_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - inital_time
        print("passed " + str(time_elapsed.total_seconds()) + " seconds")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass
    
@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre='Marco'):
    print("Hola " + nombre)
    
    
if __name__=='__main__':
    random_func()
    suma(5,5)
    saludo("Marco")
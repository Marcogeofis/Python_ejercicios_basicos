# serie de fibonacci
import matplotlib.pyplot as plt

def fibonacci(n):
    # varibles a, b
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        print(a, end=' ')
        a, b = b, a+b
        
    plot_fibo(result)
    #return result
        
def plot_fibo(n):
    val_x = []
    for i in range(len(n)):
        val_x.append(i)
        
    plt.plot(val_x, n)
    plt.title("Gráfica de Fibonacci")
    plt.xlabel("variable a")
    plt.ylabel("variable b")
    plt.show()

if __name__ == '__main__':
    numero = input('¿Hasta que número quieres que muestre la serie fibonacci? ')
    numero = int(numero)
    fibonacci(numero)
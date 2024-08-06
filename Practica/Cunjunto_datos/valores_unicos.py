a = [1,2,3,4,3,2,1]
b = ['Pera', 'Manzana', 'Lapíz', 'Pera', 'Sandía', 'Manzana']
dicc = {}
def valores_unicos(array):
    for i in array:
        if i in dicc:
            dicc[i] += 1
        else:
            dicc[i] = 1
    return dicc

if __name__ == '__main__':
    res = valores_unicos(b)
    for numero, repeticiones in res.items():
        print(f'El número {numero} se repite {repeticiones} veces en la lista.')
        
    print(res.items())
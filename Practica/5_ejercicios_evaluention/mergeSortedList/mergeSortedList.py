"""
Tu solución para fusionar dos listas ordenadas y devolver una lista ordenada funciona, pero se puede mejorar en términos de eficiencia y claridad. Aquí hay algunas recomendaciones:

Evitar modificar las listas originales: Actualmente, tu código modifica li_1 al agregarle elementos de li_2. Es preferible no modificar las listas originales y en su lugar crear una nueva lista.
Fusión eficiente: Dado que ambas listas están ordenadas, puedes fusionarlas en una sola lista ordenada de manera más eficiente sin tener que usar sorted() al final. Esto se hace utilizando un enfoque similar al algoritmo de "merge" en la ordenación por mezcla (merge sort).

"""

def merge_sorted_list(li1, li2):
        
    for el in li_2:
        li_1.append(el)
    
    return sorted(li_1)



if __name__ == '__main__':
    li_1 = list((1,3,5))
    li_2 = list((2,4,6))
    print("Lista 1", li_1)
    print("Lista 2", li_2)
    sorted_list = merge_sorted_list(li_1, li_2)
    print(f'La unión de la lista y ordenada es {sorted_list}')


def merge_sorted_list(li1, li2):
    merged_list = []
    i, j = 0, 0
    
    # Fusionar los elementos de ambas listas en orden
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            merged_list.append(li1[i])
            i += 1
        else:
            merged_list.append(li2[j])
            j += 1

    # Agregar los elementos restante de li1, si hay
    while i < len(li1):
        merged_list.append(li1[i])
        i += 1
    
    while j < len(li2):
        merged_list.append(li2[j])
        j += 1
        
    return merged_list

if __name__ == '__main__':
    li_1 = list((1,3,5))
    li_2 = list((2,4,6))
    print("Lista 1", li_1)
    print("Lista 2", li_2)
    sorted_list = merge_sorted_list(li_1, li_2)
    print(f'La unión de la lista y ordenada es {sorted_list}')

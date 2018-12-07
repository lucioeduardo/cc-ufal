def selection_sort(lista):
    tam = len(lista)
    for i in range(tam):
        m=i
        for j in range(i,tam):
            if(lista[j] < lista[m]):
                m=j
        lista[m],lista[i] = lista[i],lista[m]
    return lista

print(selection_sort([1,3,-5,-52,88,70,800,-999]))

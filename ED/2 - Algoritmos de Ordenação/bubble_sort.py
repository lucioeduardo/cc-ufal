def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(tam-i-1):
            if(lista[j] > lista[j+1]):
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista

print(bubble_sort([90,1,3,-5,-3,-52,88,70,800,-999]))

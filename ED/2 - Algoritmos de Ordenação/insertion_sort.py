def insertion_sort(lista):
    for i in range(len(lista)):
        j = i
        while(j > 0 and lista[j] < lista[j-1]):
            lista[j],lista[j-1] = lista[j-1],lista[j]
            j-=1
    return lista

print(insertion_sort([1,3,-5,-52,88,70,800,-999]))

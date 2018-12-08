def shell_sort(lista):
    size = len(lista)

    h=1
    while(3*h + 1 < size):
        h = 3*h+1

    while(h >= 1):
        for i in range(h,size):
            j = i
            while(j - h >= 0 and lista[j] < lista[j-h]):
                lista[j],lista[j-h] = lista[j-h],lista[j]
                j -= h
        h = h//3

    return lista

print(shell_sort([1,3,-5,-52,88,70,8,800,-999]))

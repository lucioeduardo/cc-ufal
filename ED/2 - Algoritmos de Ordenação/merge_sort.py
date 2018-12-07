lista = [1,3,-5,-52,88,70,800,-999]

def merge_sort(lista):
    if(len(lista) > 1):
        meio = len(lista)//2
        l1 = merge_sort(lista[:meio])
        l2 = merge_sort(lista[meio:])
        return merge(l1,l2)
    return lista

def merge(a, b):
    i=0;j=0
    aux = []
    while(i < len(a) and j < len(b)):
        if(a[i] < b[i]):
            aux.append(a[i]); i+=1
        else:
            aux.append(b[j]); j+=1
    while(i<len(a)):
        aux.append(a[i]); i+=1
    while(j<len(b)):
        aux.append(b[j]); j+=1
    return aux

print(merge_sort(lista))

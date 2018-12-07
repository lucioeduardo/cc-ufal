def quick_sort(lista, beg, end):
    if(beg < end):
        v = partition(lista,beg,end)
        quick_sort(lista, beg, v-1)
        quick_sort(lista, v+1, end)
    return lista


def partition(lista, beg, end):
    pivot = lista[beg]
    print(beg,pivot,lista[beg])
    left = beg-1
    right = end+1

    while left < right:
        left+=1
        while(left <= end and lista[left] < pivot):
            left += 1

        right-=1
        while(right >= beg and lista[right] > pivot):
            right -= 1

        if left<right:
            lista[left],lista[right] = lista[right],lista[left]

    return right



l = [80,5,10,15,20,8]

print(quick_sort(l, 0, 5))
print(l)

"""
Implemente uma função recursiva que, dada uma lista
de inteiros ordenada, busque por um valor
"""

#Busca binária - O(log n)
def bin_search(v, l):
    mid = len(l)//2
    if(len(l) == 0):
        return False

    if(l[mid] == v):
        return True
    if(l[mid] < v):
        return bin_search(v, l[mid+1:])
    return bin_search(v, l[:mid])

print(bin_search(280,[1,2,5,90,180,280]))

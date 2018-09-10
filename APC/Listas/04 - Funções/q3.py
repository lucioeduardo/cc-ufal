"""
Escreva um programa que possui uma função
que recebe uma lista e diz qual a soma máxima
entre dois elementos da lista
"""

def soma_maxima(lista):
    res = lista[0]+lista[1]
    for i in range(2,len(lista)):
        if(lista[i] + lista[i-1] > res):
            res = lista[i] + lista[i-1]
    return res

lista = [1,2,3,-50,-10,20]
print(soma_maxima(lista))

"""
Escreva um programa que possui uma função
que recebe uma lista e diz qual a soma máxima
entre dois elementos da lista
"""

def maior(lista):
    res = 0
    for i in range(0,len(lista)):
        if lista[i] > lista[res]:
            res = i
    return res

lista = [1,2,3,50,-10,20]

idx_m = maior(lista)
res = lista[idx_m]

lista[idx_m] = float("-inf") #infinito negativo, pra garantir que nao sera escolhido o mesmo numero.

idx_m2 = maior(lista)
res += lista[idx_m2]

print(res)

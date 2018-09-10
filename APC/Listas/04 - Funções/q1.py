"""
Escreva um programa que possui uma função
“maior”, que recebe uma lista e devolve o maior
elemento na lista
"""
def maior(lista):
    res = lista[0]
    for i in lista:
        if i > res:
            res = i
    return res

print(maior([-1,-2,-3,-888,-500]))

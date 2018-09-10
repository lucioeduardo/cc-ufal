"""
Escreva um programa que possui uma função
que recebe uma lista e um valor e verifica se
existe o valor na lista
"""
def exists(lista, v):
    for i in lista:
        if(i == v):
            return True
    return False

lista = [1,2,3,50,10,20]
print(exists(lista,4))

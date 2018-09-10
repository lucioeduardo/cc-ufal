"""
Faça um algoritmo que copie o conteúdo de
uma lista para outra, eliminando valores
repetidos. Implemente funções para isso
"""

def copiar(origem, destino):
    destino.clear()
    for i in origem:
        flag = True
        for j in destino:
            if(i == j):
                flag = False
        if(flag):
            destino.append(i)

a = [1,2,3,3,2,5]
b=[5,6,7]
copiar(a,b)
print(b)

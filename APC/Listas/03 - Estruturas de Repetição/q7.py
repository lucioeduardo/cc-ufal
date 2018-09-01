"""
Faça um programa que recebe um conjunto de inteiros e
verifica se existe algum número negativo no conjunto
"""
lista = [1,50,20,30,8,2,4]

existe = False

for i in lista:
    if(i < 0):
        existe = True

if(existe):
    print("Existe")
else:
    print("Não existe")

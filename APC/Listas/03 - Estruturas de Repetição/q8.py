"""
Faça um programa que recebe um conjunto de
inteiros e um valor n e verifica se existe algum
número com valor maior que n no conjunto
"""
lista = [1,2,3,4,5,6,7,8,9]
n = int(input())

existe = False
for i in lista:
    if(i>n):
        existe = True

if(existe):
    print("Existe")
else:
    print("Não existe")

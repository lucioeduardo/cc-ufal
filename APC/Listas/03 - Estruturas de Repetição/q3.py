"""
Faça um programa que recebe um conjunto de
inteiros e imprime os valores que estão abaixo da
média do conjunto
"""
lista = [1,2,3,10,15,20,15,10,5,8,9,11]

media = 0
for i in lista:
    media += i

media /= len(lista)

print("Valores abaixo da média:")
for i in lista:
    if(i < media):
        print(i)

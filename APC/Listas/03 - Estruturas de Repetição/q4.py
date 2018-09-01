"""
 Faça um programa programa que recebe um conjunto de
inteiros e conta quantos elementos maiores que n existem no
conjunto
"""
lista = [1,20,31,14,85,6,17,6,9,25]
n = int(input())

cont = 0
for i in lista:
    if(i > n):
        cont+=1

print(cont)

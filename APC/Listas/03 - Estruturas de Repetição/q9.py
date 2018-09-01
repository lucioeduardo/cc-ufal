"""
Faça um programa que recebe um conjunto de
inteiros e um valor n e indica qual o valor mais
próximo de n no conjunto
"""
lista = [10, 15, -5, 8, 200, 150, 70, 30, -8]
n = int(input())

res = lista[0]

for i in lista:
    if(abs(i-n) < abs(res-n)):
        res = i

print(res)

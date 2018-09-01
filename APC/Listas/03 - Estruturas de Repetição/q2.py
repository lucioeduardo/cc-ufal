"""
Faça um programa que conta o número de
valores negativos em um conjunto
"""
lista = [1,2,-5,3,-8,-2,15,20,-10,50,-1]

cont = 0
for i in lista:
    if i<0:
        cont+=1

print(cont)

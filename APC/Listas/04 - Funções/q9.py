"""
Faça um programa que tenha duas funções,
uma para calcular a média e outra para calcular a
variância de um conjunto de números
"""

def media(lista):
    res=0
    for i in lista:
        res += i
    return res/len(lista)

def variancia(lista):
    med = media(lista)
    res = 0
    for i in lista:
        res += (i-med)**2
    return res/len(lista)

lista = [70,60,88,32,64]
print("%.2f"%variancia(lista))

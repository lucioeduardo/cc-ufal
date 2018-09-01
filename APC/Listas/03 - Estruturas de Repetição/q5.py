"""
Faça um programa que recebe um conjunto de inteiros e
calcula a amplitude do conjunto.
"""
lista = [5,2,1,20,18,15,13,8,9,11]

maior=lista[0]
menor=lista[0]

for i in lista:
    if(i > maior):
        maior=i
    if(i < menor):
        menor=i

print("Amplitude:",maior-menor)

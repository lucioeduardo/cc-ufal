"""
Algoritmo que recebe uma palavra e imprime o
reverso dessa palavra
"""
palavra = input()

reverso = ""
i = len(palavra)-1

while(i >= 0):
    reverso += palavra[i]
    i-=1

print(reverso)

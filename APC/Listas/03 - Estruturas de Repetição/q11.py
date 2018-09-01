"""
Algoritmo que recebe uma palavra e um
caractere e conta as ocorrências do caractere na
palavra
"""
palavra = input()
char = input()

cont = 0
for i in palavra:
    if(i == char):
        cont+=1

print(cont)

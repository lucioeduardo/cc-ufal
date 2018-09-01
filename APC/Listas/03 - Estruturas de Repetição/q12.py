"""
Algoritmo que recebe uma palavra e conta quantas
vogais há na palavra
"""
palavra = input()

cont=0
for i in palavra:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        cont += 1
    if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        cont += 1

print(cont)

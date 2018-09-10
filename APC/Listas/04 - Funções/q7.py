"""
Um a palavra A é dita uma permutação de uma
palavra B se os caracteres de A formam uma
permutação dos caracteres de B
– Ex: amor é uma permutação de roma
– Ex: metro é uma permutação de morte
– Faça uma função conta_caracteres que recebe uma
palavra e um caractere e conta quantas vezes ele
aparece na palavra
"""
def conta_caracteres(palavra, c):
    res=0
    for i in palavra:
        if(i == c):
            res+=1
    return res

print(conta_caracteres("amora", "a"))

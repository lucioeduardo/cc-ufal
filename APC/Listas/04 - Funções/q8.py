"""
Usando a função do item anterior, faça um
programa que recebe duas palavras e responda
se uma é permutação da outra.
"""
def conta_caracteres(palavra, c):
    res=0
    for i in palavra:
        if(i == c):
            res+=1
    return res

p1 = input()
p2 = input()

flag = True

if(len(p1) != len(p2)):
    flag=False
else:
    for i in p1:
        if(conta_caracteres(p1,i) != conta_caracteres(p2,i)):
            flag = False

if(flag):
    print("É permutação")
else:
    print("Não é permutação")

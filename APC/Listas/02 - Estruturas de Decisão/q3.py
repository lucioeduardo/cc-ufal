"""
3. Faça um programa que receba três palavras e ordene elas em
ordem alfabética.
"""
a = input()
b = input()
c = input()

if(a>b):
    a,b=b,a #Troca o valor de a com o de b
if(b>c):
    b,c=c,b
if(a>b):
    a,b=b,a

print("\nPalavras em ordem alfabética:")
print(a)
print(b)
print(c)

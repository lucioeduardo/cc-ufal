"""
Escreva um algoritmo que recebe três valores para os lados de um
triângulo (a,b e c) e decide se a forma geométrica é um triângulo ou não e em
caso positivo, classifique em isósceles, escaleno ou equilátero.
– O valor de cada lado deve ser menor que' a soma dos outros dois
– Isósceles: dois lados iguais e um diferente
– Escaleno: todos os lados diferentes
– Equilátero: todos os lados iguais
"""
a = int(input("Valor de A:"))
b = int(input("Valor de B:"))
c = int(input("Valor de C:"))

if((a < b+c) and (b < a+c) and (c < a+b)):
    if(a == b and b == c):
        print("Triângulo Equilátero")
    elif(a == b or b == c or a == c):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é triângulo")

"""
2. Faça um programa que leia a idade de uma pessoa e
imprima sua categoria:
– Criança, se menor de 14 anos
– Adolescente, se entre 14 e 17 anos
– Adulto, se entre 18 e 59 anos
– Idoso, se maior que 60 anos
"""
idade = int(input("Idade:"))

if(idade < 14):
    print("Criança")
elif(idade <= 17):
    print("Adolescente")
elif(idade <= 59):
    print("Adulto")
else:
    print("Idoso")

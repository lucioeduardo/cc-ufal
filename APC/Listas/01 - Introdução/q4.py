"""
Faça um algoritmo que leia dois valores para as
variáveis A e B e efetue a troca dos valores de
forma que a variável A passe a possuir o valor da
variável B e a variável B passe a possuir o valor
da variável A. Apresente os valores trocados.
"""
a = input()
b = input()

aux = a
a = b
b = aux

print(a, b)

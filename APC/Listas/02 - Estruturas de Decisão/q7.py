"""
Uma das tarefas de um caixa eletrônico é decidir
qual a combinação de cédulas deve fornecer ao
usuário quando este solicita um saque, de modo a
minimizar o número de cédulas fornecidas.
Sabendo que um caixa eletrônico possui notas de
100, 50, 10, 5 e 1, faça um programa que recebe
um valor a ser sacado e decida qual a combinação
de cédulas irá fornecer.
"""
valor = int(input("Valor:"))

print(valor//100, "nota(s) de 100")
valor %=100

print(valor//50, "nota(s) de 50")
valor%=50

print(valor//10, "nota(s) de 10")
valor%=10

print(valor//5, "nota(s) de 5")
valor%=5

print(valor, "nota(s) de 1")

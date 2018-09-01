"""
Uma empresa de vendas tem vários corretores. A empresa paga
ao corretor uma comissão calculada de acordo com o valor de suas
vendas. Se o valor da venda de um corretor for maior que R$
50.000.00 a comissão será de 12% do valor vendido. Se o valor da
venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 a
comissão será de 9.5%. Em qualquer outro caso, a comissão será
de 7%. Escreva um programa que recebe o nome e o valor vendido
por um corretor e indique qual será sua comissão
"""
nome = input("Nome:")
valor = float(input("Valor:"))
comissao = 0

if(valor > 50000):
    comissao = valor*0.12
elif(valor >= 30000):
    comissao = valor*0.095
else:
    comissao = valor*0.07

print("Comissão: %.2f" %comissao)

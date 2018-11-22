"""
2. Contar o número de elementos negativos em um conjunto

*** Análise ***
Operação principal: condição que define se o numero é negativo
T(n) = n
"""

lista = [1,2,3,-1,-2,4]

cont = 0

for i in lista:
    if(i < 0):
        cont += 1

print(cont)

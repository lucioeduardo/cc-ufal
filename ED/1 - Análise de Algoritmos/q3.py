"""
3. Identificar os valores de um conjunto que estão abaixo da
média do conjunto

*** Análise ***
Operação principal: comparação i < med
T(n) = n
"""

lista = [1,2,3,59,2,4,76,14,31]

med = 0

for i in lista:
    med += i

med /= len(lista)

for i in lista:
    if i < med:
        print(i)

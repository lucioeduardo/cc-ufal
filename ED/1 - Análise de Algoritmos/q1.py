"""
1. Calcular o fatorial de um número

*** Análise ***
A operação principal é executada n-1 vezes(de 2 até n), então
T(n) = n-1
"""

n = int(input())

fat = 1
for i in range(2,n+1):
    fat *= i #Operação principal

print(fat)

"""
5. Copiar uma lista de inteiros, retirando elementos repetidos

*** Análise ***
Operação principal: comparação j == i
T(n) = n²
"""
conj = [1,2,2,5,2,8,3,4,1,9]
copy = []
for i in conj:
    flag = True
    for j in copy:
        if j == i:
            flag=False
    if(flag):
        copy.append(i)

print(copy)

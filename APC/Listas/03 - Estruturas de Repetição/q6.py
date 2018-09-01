"""
Faça um algoritmo que recebe dois conjuntos de inteiros A
e B e calcula a distância euclidiana entre estes dois conjuntos
"""
a = [1,2,3,4,5]
b = [1,5,2,1,10]

dist = 0

for i in range(0,len(a)):
    dist += (a[i]-b[i])**2

print("Distância:" + dist)

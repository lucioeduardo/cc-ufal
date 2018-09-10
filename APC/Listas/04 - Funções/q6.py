"""
6. Percebendo que o método anterior de cálculo
de notas foi muito severo, o professor decidiu
mudar o formato do cálculo. A nova fórmula foi:
– Nota = (nota/max)*10
– Faça um programa para calcular as notas dos
alunos segundo essa nova regra, utilizando
funções
"""

def maior(lista):
    res = lista[0]
    for i in lista:
        if i > res:
            res = i
    return res

def calc_nota(nota, nota_max):
    return 10*(nota/nota_max)

notas = [1,4,3,5,7,8,9,8,8,5,2]
resultado = []

nota_max = maior(notas)

for i in notas:
    resultado.append(calc_nota(i, nota_max))

print(resultado)

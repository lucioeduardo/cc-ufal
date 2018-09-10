"""
Um professor teve uma ideia de como avaliar seus
alunos em uma atividade que vale entre 0 e 10 de modo
a incentivar a competição entre os alunos. Quem tirar a
maior nota terá 10. Quem tirar a menor nota, terá 0. As
outras notas serão algo entre 0 e 10 da seguinte forma:
● Nota = ((nota-min)/(max – min))*10 <-- [Essa fórmula ja garante que quem tirar a
nota máxima fica com 10 e quem tirar a minima, com 0.]
● Faça um programa para calcular as notas dos alunos
segundo essa regra, utilizando funções
"""
def maior(lista):
    res = lista[0]
    for i in lista:
        if i > res:
            res = i
    return res

def menor(lista):
    res = lista[0]
    for i in lista:
        if i < res:
            res = i
    return res

def calc_nota(nota, nota_min, nota_max):
    return 10*(nota-nota_min)/(nota_max-nota_min)

notas = [1,4,3,5,7,8,9,8,8,5,2]
resultado = []

nota_min = menor(notas)
nota_max = maior(notas)
for i in range(0, len(notas)):
    resultado.append(calc_nota(notas[i], nota_min, nota_max))
print(resultado)

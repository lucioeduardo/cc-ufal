dic = {}

def media(nome):
    return sum(dic[nome])/len(dic[nome])

while True:
    nome = input("Nome do aluno:")
    if(nome == ""):
        break

    notas = list(map(int,input("Digite as notas separadas por espaço:").split()))
    dic[nome] = notas

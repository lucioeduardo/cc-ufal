lista = {}

def incluirNovoNome(nome, telefones):
    lista[nome] = telefones

def incluirTelefone(nome, telefone):
    if(nome in lista):
        lista[nome].append(telefone)
    else:
        add = input("Nome inexistente na lista, deseja adicionar? (s/n):")
        if(add.lower() == "s"):
            incluirNovoNome(nome,[telefone])

def excluirTelefone(nome, telefone):
    lista[nome].remove(telefone)
    if(len(lista[nome]) == 0):
        excluirNome(nome)

def excluirNome(nome):
    lista.pop(nome)

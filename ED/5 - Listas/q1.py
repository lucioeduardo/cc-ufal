from lista_encadeada import Lista

def construct(vetor):
    l = Lista()

    for i in vetor:
        l.push_back(i)

    return l

l = construct([1,2,3,4])

l.print_list()
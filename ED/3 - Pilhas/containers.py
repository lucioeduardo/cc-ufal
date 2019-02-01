from dynamic_stack import Stack

containers = ["C-" + str(x) for x in range(1,11)]
pilhas = [Stack() for i in range(0,4)]
swap = Stack()

def escolhe_pilha():
    res = 0
    for i in range(0,4):
        res = i if pilhas[i].size < pilhas[res].size else res
    return res

def desempilha(container, pilha):
    p = pilhas[pilha]
    v = ""
    while(v != container):
        v = p.pop()
        swap.push(v)
    
    swap.pop()
    
    while(not swap.empty()):
        p.push(swap.pop())

for i in containers:
    print("Pushing",i,"on",escolhe_pilha())
    pilhas[escolhe_pilha()].push(i)

for i in pilhas:
    print("Pilha:")
    i.print_all()

desempilha("C-1",0)

print("\n")

for i in pilhas:
    print("Pilha:")
    i.print_all()
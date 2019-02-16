class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def push(self, value):
        node = Node(value)
        if(self.empty()):
            self.front = node
        else:
            self.back.next = node
        self.back = node
    
    def pop(self):
        if(self.empty()):
            print("Queue is empty")
            return 
        
        value = self.front.value
        self.front = self.front.next
        
        return value
    
    def empty(self):
        return self.front == None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

normal = Queue()
prioridade = Queue()

while(True):
    inp = input("Digite uma senha ou 0 para finalizar:")
    if(inp == "0"):
        break
    elif(inp[0] == "n"):
        normal.push(inp)
    else:
        prioridade.push(inp)
        

print("Ordem de prioridade:")

while(not(normal.empty() and prioridade.empty())):
    if(not prioridade.empty()):
        print(prioridade.pop())
    if(not normal.empty()):
        print(normal.pop())

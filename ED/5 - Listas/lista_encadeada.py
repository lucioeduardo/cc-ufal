class Lista:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def push_back(self,value):
        no = Node(value)
        self.size += 1

        if(self.empty()):
            self.front = no
        else:
            self.back.next = no
        self.back = no

    def push_front(self, value):
        no = Node(value)
        self.size += 1

        no.next = self.front
        self.front = no
    
    def push(self, value, idx):
        if(idx >= self.size):
            return None
        self.size += 1
        aux = self.front
        while(idx > 1 ):
            idx -= 1
            aux = aux.next
        
        no = Node(value)
        no.next = aux.next
        aux.next = no

    def get(self, idx):
        if(idx >= self.size):
            return None
        
        aux = self.front
        while(idx):
            idx-=1
            aux = aux.next
        
        return aux.value
    
    def remove(self, idx):
        if(idx >= self.size):
            return None
        
        aux = self.front
        while(idx>1):
            idx-=1
            aux = aux.next
        
        value = aux.next.value
        aux.next = (aux.next).next
        
        return value

    def print_list(self):
        aux = self.front

        while(aux != None):
            print(aux.value)
            aux = aux.next

    def empty(self):
        return (self.front == None)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
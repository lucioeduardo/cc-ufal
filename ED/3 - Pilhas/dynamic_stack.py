class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        item = Node(value)
        item.next = self.top
        self.top = item
        self.size+=1
    
    def pop(self):
        if(self.empty()):
            print("Empty stack.")
            return
        
        self.size -= 1
        item = self.top
        self.top = self.top.next
        return item.value
    
    def empty(self):
        return True if self.top == None else False

    def print_all(self):
        item = self.top
        while(item != None):
            print(item.value)
            item = item.next
    
    def get_size(self):
        return self.size

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
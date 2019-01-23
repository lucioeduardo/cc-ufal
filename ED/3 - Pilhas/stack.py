class Stack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.stack = [None]*size
    
    def push(self,item):
        if(self.full()):
            print("Stack is full")
            return None
        self.stack[self.top] = item
        self.top += 1
    
    def pop(self):
        if(self.empty()):
            print("Stack empty")
            return None
        self.top -= 1
        return self.stack[self.top]

    def empty(self):
        return True if self.top == 0 else False

    def full(self):
        return True if self.top == self.size else False 

    def print_all(self):
        print(self.stack[:self.top])
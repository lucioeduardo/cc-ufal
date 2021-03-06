class Queue:
    def __init__(self, size):
        self.size = size+1 #Mais um pois é preciso um indice para guardar o final da lista.
        self.begin = 0
        self.end = 0
        self.queue = [None]*(self.size)
    
    def push(self, value):
        if(self.full()):
            print("Queue is full")
            return
        self.queue[self.end]=value
        self.end = (self.end+1) % self.size

    def pop(self):
        if(self.empty()):
            print("Queue is empty.")
            return None
        value = self.queue[self.begin]
        self.begin = (self.begin+1) % self.size
        return value

    def empty(self):
        return self.begin == self.end
    
    def full(self):
        return self.end == (self.begin-1)%self.size

    def print_queue(self):
        print (self.queue, self.begin, self.end)

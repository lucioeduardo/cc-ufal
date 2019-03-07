class Lista():
    def __init__(self, size):
        self.size = size
        self.lista = [None]*size
        self.end = 0
    
    def insert(self, value, idx):
        if(self.end == self.size):
            return
        for i in range(self.end,idx,-1):
            self.lista[i] = self.lista[i-1]
        self.lista[idx] = value
        self.end += 1
    
    def remove(self, idx):
        if(self.end <= idx):
            return
        for i in range(idx, self.end-1):
            self.lista[i] = self.lista[i+1]
        
        self.end-=1
    
    def push_back(self, value):
        if(self.end == self.size):
            return
        
        self.lista[self.end] = value
        self.end += 1
    
    def get(self, idx):
        return self.lista[idx]
    
    def print_list(self):
        print(self.lista)
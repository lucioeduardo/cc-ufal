class HashTable():
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def hash(self, key):
        return key % self.size
    
    def insert(self, key):
        idx = self.hash(key)
        if(self.table[idx] == None):
            self.table[idx] = []

        self.table[idx].append(key)
    
    def remove(self, key):
        idx = self.hash(key)
        self.table[idx].remove(key)
    
    def print_table(self):
        for i in range(0,self.size):
            print(i,  "|", self.table[i])
        print(self.table)
        print()

h = HashTable(10)

h.insert(5)
h.insert(15)
h.insert(25)

h.print_table()

h.remove(15)

h.print_table()



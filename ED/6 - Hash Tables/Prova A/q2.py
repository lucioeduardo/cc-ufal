class HashTable():
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def hash(self, key):
        s = 0
        for i in key:
            s += ord(i)
        return s % self.size

    def insert(self, key):
        index = self.hash(key)
        if(self.table[index] == None):
            self.table[index] = []
        for i in self.table[index]:
            if(i.key == key):
                i.value += 1
                return
        pair = Pair(key) 
        self.table[index].append(pair)

    def remove(self, key):
        index = self.hash(key)
        if(self.table[index] != None):
            self.table[index].remove(key)        

    def print_table(self):
        for i in range(self.size):
            if(self.table[i] != None):
                for j in self.table[i]:
                    print(j.key, "|", j.value)

class Pair():
    def __init__(self, key):
        self.key = key
        self.value = 1


votos=["basquete","futebol","futebol","basquete","judo","volei","futebol","basquete","futebol","volei",
"judo","judo","futebol","ciclismo","judo"]

table = HashTable(10)

for i in votos:
    table.insert(i)

table.print_table()
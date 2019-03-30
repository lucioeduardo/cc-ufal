class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=[('L',None)]*size
        self.length=0
    
    def hash(self, pos):
        return pos % self.size

    def full(self):
        return self.length == self.size

    def empty(self):
        return self.length == 0

    def insert(self, key):
        if(self.full()):
            return
        for i in range(0,self.size):
            idx = self.hash(key+i)
            if(self.table[idx][0] != 'O'):
                self.table[idx] = ('O',key)
                self.length += 1
                break
    
    def remove(self, key):
        if(self.empty()):
            return

        for i in range(0, self.size):
            idx = self.hash(key+i)
            if(self.table[idx][0] == 'L'):
                return 
            if(self.table[idx][1] == key):
                self.table[idx] = ('R',None)
                self.length -= 1
                return
    

    def print_table(self):
        for i in self.table:
            print(i[0], "|", i[1])
        print()

# t = HashTable(5)

# t.insert(15)
# t.insert(19)
# t.remove(19)
# t.print_table()

tabela =  HashTable(5)
tabela.print_table()
tabela.insert(16)
tabela.insert(23)
tabela.insert(41)
tabela.insert(25)
tabela.insert(39)
tabela.insert(49)
tabela.insert(59)
tabela.print_table()
tabela.remove(41)
tabela.remove(23)
tabela.remove(62)
tabela.remove(25)
tabela.remove(39)
tabela.print_table()
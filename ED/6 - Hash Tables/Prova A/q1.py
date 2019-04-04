class HashTable():
    def __init__(self, size, sum):
        self.size = size
        self.table = [None]*size
        self.sum = sum
    
    def hash(self, key):
        last_two = key % 100
        first_two = key // 100
        return (last_two + first_two)%10 if self.sum else (last_two*first_two) % 10

    def insert(self, key):
        index = self.hash(key)
        if(self.table[index] == None):
            self.table[index] = []
        self.table[index].append(key)

    def remove(self, key):
        index = self.hash(key)
        if(self.table[index] != None):
            self.table[index].remove(key)        

    def print_table(self):
        for i in range(self.size):
            print(i, "|", self.table[i])


table = HashTable(10, True)

table.insert(5150)
table.insert(1523)
table.insert(3123)
table.insert(1345)

table.print_table()

table = HashTable(10, False)

table.insert(5150)
table.insert(1523)
table.insert(3123)
table.insert(1345)

table.print_table()
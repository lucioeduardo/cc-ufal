class List:
	def __init__(self):
		self.size=0
		self.front=None
		
	def empty(self):
		return self.size == 0
	
	def insert(self, value, *pos):
		pos = pos[0] if pos != () else self.size
		
		if(pos > self.size):
			return None
		
		no = Node(value)
		
		if(pos == 0):
			no.next = self.front
			self.front = no
		else:
			aux = self.front
			for i in range(pos-1):
				aux = aux.next
			
			no.next = aux.next
			aux.next = no
		self.size += 1
	
	def remove(self, pos):
		if(pos >= self.size):
			return None
			
		value = 0
		
		if(pos == 0):
			value = self.front.value
			self.front = self.front.next
		else:
			aux = self.front
			for i in range(pos-1):
				aux = aux.next
			
			value = aux.next.value
			aux.next = aux.next.next
		self.size -= 1
		return value
	
	def print_list(self):
		aux = self.front
		while(aux != None):
			print(aux.value)
			aux = aux.next
		
	def exists(self, value):
		aux = self.front
		while(aux != None):
			if(aux.value == value):
				return True
			aux = aux.next
		return False
		

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

lista = List()
valores = [1,2,8,50,15,20,5,4]
x = 24

for i in valores:
	lista.insert(i)

flag = False
while(not lista.empty() and not flag):
	value = lista.remove(0)
	if(lista.exists(x-value)):
		flag = True
		print("%d+%d=%d"%(value,x-value,x))

if(not flag):
	print("Não existe")







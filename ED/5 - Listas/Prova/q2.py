class List:
	def __init__(self):
		self.size=0
		self.front=None
		
	def empty(self):
		return self.size == 0
	
	def insert(self, name, phone):
		no = Node(name, phone)
		
		if(self.empty() or no.name < self.front.name):
			no.next = self.front
			self.front = no
		else:
			aux = self.front
			while(aux.next != None and aux.next.name < no.name):
				aux = aux.next
			no.next = aux.next
			aux.next = no 
		
		self.size+=1
	
	def print_list(self):
		aux = self.front
		while(aux != None):
			print(aux.name, aux.phone)
			aux = aux.next

class Node:
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone
		self.next = None		

lista = List()

while True:
	name = input("Digite o nome do novo contato ou 0 para encerrar:")
	
	if(name == "0"):
		break
	
	phone = input("Digite o telefone:")
	
	lista.insert(name,phone)
	
	print("\nLista telefônica:")
	lista.print_list()
	print("\n")








		
		

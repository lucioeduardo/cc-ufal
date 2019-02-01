from dynamic_stack import Stack

palavra = input()
tam = len(palavra)


s = Stack()

for i in range(0, tam//2):
    s.push(palavra[i])

if(tam % 2):
    i+=1

flag = True
for j in range(i+1,tam):
    if(palavra[j] != s.pop()):
        flag = False

print("Palindromo" if flag else "Nào palindromo")
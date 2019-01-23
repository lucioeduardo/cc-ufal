from stack import Stack

p = Stack(50)

exp = input()
res = True

for i in exp:
    p.print_all()
    if(i in "{[("):
        p.push(i)
    elif(i == ")" and p.pop() != "("):
        res = False
    elif(i == "]" and p.pop() != "["):
        res = False
    elif(i == "}" and p.pop() != "{"):
        res = False

print("Bem formada" if res else "Mal formada")
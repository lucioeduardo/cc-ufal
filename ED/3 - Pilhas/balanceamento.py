from static_stack import Stack

p = Stack(50)

exp = input()
res = True

for i in exp:
    if(i in "{[("):
        p.push(i)
    elif(i == ")" and p.pop() != "("):
        res = False
    elif(i == "]" and p.pop() != "["):
        res = False
    elif(i == "}" and p.pop() != "{"):
        res = False

res = res and p.empty()

print("Bem formada" if res else "Mal formada")
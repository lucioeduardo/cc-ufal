"""
 Faça um programa que recebe um número e
calcula o fatorial desse número
"""
num = int(input())
fat=1

for i in range(2,num+1):
    fat *= i

print("%d! = %d"%(num,fat))

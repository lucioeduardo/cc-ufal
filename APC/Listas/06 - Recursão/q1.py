"""
 Implemente uma função recursiva que, dados dois
números inteiros x e n, calcule o valor de x.n
"""

def mult(x, n):
    if(n == 0):
        return 0
    return x + mult(x,n-1)

print(mult(3,7))

"""
 Implemente uma função recursiva que, dados dois
números inteiros x e n, calcule o valor de x^n
"""

#O(n) - Solução óbvia
def exp(x, n):
    if(n == 0):
        return 1
    return x*exp(x,n-1)

#O(log n) - Exponenciação rápida
def fast_exp(x, n):
    if(n == 0):
        return 1
    if(n % 2):
        return x*fast_exp(x*x,n//2)
    return fast_exp(x*x,n//2)

print(exp(3,5), fast_exp(3,5))

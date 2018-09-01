"""
-*- coding:utf-8 -*-
Faça um algoritmo que calcule e apresente o
valor do volume de uma lata de óleo, utilizando a
fórmula V = π * RAIO² * ALTURA.
"""
r = float(input("Raio:"))
h = float(input("Altura:"))
PI = 3.14159
print("Volume: %.2f" %(PI * r**2 * h))

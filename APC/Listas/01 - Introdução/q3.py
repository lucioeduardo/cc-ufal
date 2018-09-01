"""
Faça um algoritmo que calcule e apresente o
valor do volume de uma lata de óleo, utilizando a
fórmula V = π * RAIO² * ALTURA.
"""
PI = 3.14159
raio = float(input("Raio:"))
altura = float(input("Altura:"))

print("Volume: %.2f" %(PI * raio**2 * altura))

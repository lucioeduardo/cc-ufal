"""
Faça um algoritmo que leia uma temperatura
em graus Fahrenheit e apresente-a convertida
em graus Celsius.
"""
temp_f = float(input("Temperatura em Fahrenheit:"))
temp_c = (temp_f-32)*5/9
print("Temperatura em Celsius:",temp_c)

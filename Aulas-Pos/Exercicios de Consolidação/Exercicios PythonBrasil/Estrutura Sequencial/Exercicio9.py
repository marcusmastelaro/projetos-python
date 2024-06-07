# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (float(fahrenheit - 32)/1.8)

print(f"\nSua temperatura em Graus Celsius é: {celsius:.2f}")

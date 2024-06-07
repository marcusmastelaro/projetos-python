# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite sua temperatura em Graus Celsius: "))
fahrenheit = (float(celsius * 1.8) + 32)

print(f"\nSua temperatura em Fahrenheit é {fahrenheit:.2f}")

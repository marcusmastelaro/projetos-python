# Faça um Programa que leia três números e mostre o maior deles.
import numpy as np
numeros = []
for i in range(3):
    valor = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(valor)

maiornumero = max(numeros)

print(f"Os valores digitados foram {numeros} e o maior é {maiornumero}.")

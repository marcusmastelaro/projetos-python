# Faça um Programa que leia três números e mostre o maior e o menor deles.

import numpy as np
numeros = []
for i in range(3):
    valor = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(valor)

maiornumero = max(numeros)
menornumero = min(numeros)

print(f"\nOs números digitados foram: {numeros}.")
print(f"O Maior número do conjunto é: {maiornumero}. ")
print(f"O Menor número do conjunto é: {menornumero}. ")

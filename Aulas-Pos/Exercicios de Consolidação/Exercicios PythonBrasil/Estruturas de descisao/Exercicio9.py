# Faça um Programa que leia três números e mostre-os em ordem decrescente.

import numpy as np
numeros = []
for i in range(3):
    valor = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(valor)

numerosordenadosasc = sorted(numeros, reverse=False)
numerosordenadosdesc = sorted(numeros, reverse=True)

print(f"\nOs números digitados originalmente são esses: {numeros}.")
print(f"Os números digitados originalmente e ordenados em ordem crescente são esses: {
      numerosordenadosasc}.")
print(f"Os números digitados originalmente e ordenados em ordem decrescente são esses: {
      numerosordenadosdesc}.\n")

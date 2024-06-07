# ) Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import numpy as np
lista = np.zeros(10, dtype=int)
print("Situação do Vetor Atual")
print(lista)

for item in range(10):
    lista[item] = int(input(f"\nDigite um numero inteiro: "))
    print("Item %d Registrado." % (item+1))
print("\nImprime elementos na ordem correta:")
print(lista)

print("\nImprime elementos na ordem inversa:")
while (item >= 0):
    print(lista[item], end=" ")
    item -= 1

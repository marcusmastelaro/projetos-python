#  Faça um programa que leia 2 listas de tamanho 5 e crie uma terceira lista que tenha todos
# os elementos das duas listas.

import numpy as np
tam = 5
lista1 = np.zeros(tam, dtype=int)
lista2 = np.zeros(tam, dtype=int)
lista3 = np.zeros(tam*2, dtype=int)

for i in range(0, tam, 1):
    lista1[i] = int(input("Digite um numero da lista 1: "))

for j in range(0, tam, 1):
    lista2[j] = int(input("Digite um numero da lista 2: "))

for x in range(0, tam*2, 1):
    if (x < tam):
        lista3[x] = lista1[x]
    else:
        lista3[x] = lista2[x-tam]
print("Vetor 1: ", lista1)
print("Vetor 2: ", lista2)
print("Vetor 3: ", lista3)

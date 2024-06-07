# Faça um programa que leia um valor T e preencha uma lista N[20] com a sequência de valores de 0 até T-1
# repetidas vezes, conforme exemplo: T3=3, vector = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,2, 0, 1, 2, 0, 1, 2, 0, 1]

import numpy as np
lista = 20
T = np.zeros(lista, dtype=int)
valor = int(input("Digite um valor: "))
cont = 0

while cont < lista:
    for i in range(0, valor, 1):
        T[cont] = i
        cont += 1
        if (cont == lista):
            break
print(T)

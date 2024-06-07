# Faça um programa que leia um vetor X[10]. Substitua, a seguir, todos os valores nulos e
# negativos do vetor X por 1. Em seguida, mostre o vetor X.

import numpy as np
x = np.zeros(10)

for i in range(0, 10):
    x[i] = int(input("Digite um numero: "))
    if x[i] < 0:
        x[i] = 1
print(x)

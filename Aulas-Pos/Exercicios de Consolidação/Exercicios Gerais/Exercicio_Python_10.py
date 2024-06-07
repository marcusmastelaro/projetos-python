# Faça um programa que leia a idade de 5 pessoas e imprima na tela quantas já atingiram a maioridade

import numpy as np

print("Informe a idade de 5 pessoas: ")
vetor = np.zeros(5, dtype=int)
maioridade = 18
numMaior = 0

for i in range(0, 5, 1):
    vetor[i] = int(input())
    if vetor[i] >= maioridade:
        numMaior += 1
print("%d pessoas já atingiram a maioridade." % numMaior)

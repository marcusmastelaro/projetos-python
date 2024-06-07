# Faça uma função que receba um vetor de números inteiros e retorne a soma dos elementos
# do vetor.

import numpy as np


def vetor(a, dtype=int):
    soma = 0
    for i in range(0, len(a), 1):
        soma += a[i]
    return soma


num = int(input("Digite um número inteiro: "))
vetorn = np.random.randint(1, 11, num)
print(vetorn)
resultado = vetor(vetorn)
print("A soma dos elementos do vetor é: ", resultado)

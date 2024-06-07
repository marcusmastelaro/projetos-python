# 5) Faça uma função que receba um vetor de números inteiros e retorne quantos desses números são pares

import numpy as np


def checa_numeros(a):
    qtde_pares = 0
    for i in range(0, len(a), 1):
        if (a[i] % 2 == 0):
            qtde_pares += 1
    return qtde_pares


num = int(input("Digite um numero inteiro: "))
vetor = np.random.randint(1, 101, num)
print(f"\nSeu vetor atual é:", vetor)
resultado_final = checa_numeros(vetor)
print(f"\nA quantidade de numeros pares do vetor é:", resultado_final)

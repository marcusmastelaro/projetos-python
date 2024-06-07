# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical

import numpy as np
nome = input("Digite seu nome: ")
tamanho = len(nome)

for i in range(0, tamanho, 1):
    print(nome[i])
print(nome)

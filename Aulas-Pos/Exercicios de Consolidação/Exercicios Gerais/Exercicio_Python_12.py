# O bubble sort é um algoritmo de ordenação dos mais simples. A ideia é percorrer a lista diversas vezes e,
# a cada passagem, fazer flutuar para o topo o maior elemento da sequência. Dada uma lista de valores em ordem
# aleatória, use o algoritmo bubble sort para ordená-la e imprima o resultado.
import numpy as np
# import pdb

tamanho = int(input("Informe o tamanho do vetor: "))
vetor = np.random.randint(1, 101, tamanho)
print(vetor)
cont = 0
for i in range(0, tamanho-1):
    for j in range(0, tamanho-i-1):
        # cont+=1
        if (vetor[j] > vetor[j+1]):
            # pdb.set_trace()
            temp = vetor[j+1]
            vetor[j+1] = vetor[j]
            vetor[j] = temp

print(vetor)
# print(cont)

# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

import numpy as np
lista = []
for i in range(3):
    preco = float(input(f"Digite o {i+1}° preço da coca-cola: "))
    lista.append(preco)

maiorpreco = max(lista)
menorpreco = min(lista)

print(f"\nOs Preços digitados para a coca-cola foram: {lista}.")
print(f"O Maior preço da coca-cola é: {maiorpreco} Reais. ")
print(f"O Menor preço da coca-cola é: {menorpreco} Reais. ")
print(
    f"\nRecomendo fortemente a compra da coca-cola com o preço de {menorpreco} Reais")

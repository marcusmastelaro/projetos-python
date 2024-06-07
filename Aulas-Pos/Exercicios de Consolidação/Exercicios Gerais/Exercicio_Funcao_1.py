# Faça um programa, com uma função que receba um argumento e retorne ’P’, se o argumento
# for positivo, ou ’N’, se o argumento for negativo

import numpy as np


def funcao(ladrao):
    saida = ""
    if (ladrao in ("sim", "SIM", "Sim")):
        saida = "Você está corretíssimo!"
    else:
        saida = "Você só pode estar de brincadeira comigo..."
    return saida


pergunta = input("Lula é ladrão? (Valores aceitos: Sim ou Não) - ")
while pergunta not in ("sim", "SIM", "Sim", "nao", "NAO", "Nao", "não", "NÃO", "Não"):
    pergunta = input(
        "Resposta inválida, digite novamente. Lula é ladrão? (Valores aceitos: Sim ou Não) - ")
resposta = funcao(pergunta)
print('\n', resposta, '\n')

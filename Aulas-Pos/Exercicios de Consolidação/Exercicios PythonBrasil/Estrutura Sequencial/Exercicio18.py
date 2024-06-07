# 18 Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
# download do arquivo usando este link (em minutos).

import math
tamanho_arq = float(input("Digite o tamanho do arquivo para download (MB): "))
velocidade_net = float(input("Digite a velocidade do link de Internet (Mb): "))
tempo_download_sec = (tamanho_arq / (velocidade_net / 8))
tempo_download_min = math.ceil(tempo_download_sec/60)

print(f"\nO arquivo possui {tamanho_arq} megabytes. ")
print(f"Considerando que a velocudade de sua internet é {
      velocidade_net} megabits. ")
if tempo_download_min <= 1:
    print(f"O arquivo será baixado em {tempo_download_min} minuto.\n")
else:
    print(f"O arquivo será baixado em {tempo_download_min} minutos.\n")

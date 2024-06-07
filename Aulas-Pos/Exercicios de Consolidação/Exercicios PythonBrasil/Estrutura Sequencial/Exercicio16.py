# 16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.

import math
lata = 18
valorlata = 80

area = float(input("Digite a quantidade em M2 a ser pintada: "))
# 1 litro para 3 metros. Uma lata cobre 54 metros
cobertura = math.ceil(area / lata)
valortotal = (cobertura * valorlata)

if cobertura <= 1:
    print(f"\nVocê precisará de apenas {
          cobertura:.2f} lata de tina de 18 litros.")
else:
    print(f"Você precisará de {cobertura:.2f} latas de tinta de 18 litros.")
print(f"Seu orçamento ficou {valortotal:.2f} Reais.")

# 17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#  a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
lata = 18
galao = 3.6
valorlata = 80
valorgalao = 25

area = float(input("Digite a quantidade em M2 a ser pintada: "))
# 1 litro para 6 metros. Uma lata cobre 108 metros
coberturalata = math.ceil(area / lata)
valortotallata = (coberturalata * valorlata)
coberturagalao = math.ceil(area / galao)
valortotalgalao = (coberturagalao * valorgalao)

escolha = input("\nInforme o tipo de produto deseja (lata, galao): ")
while escolha not in ("lata", "galao"):
    escolha = input(
        "\nTipo incorreto. Informe o tipo de produto deseja (lata, galao): ")

if escolha == "lata":
    if coberturalata <= 1:
        print(f"\nVocê precisará de apenas {
              coberturalata:.2f} lata de tinta de 18 litros.")
    else:
        print(f"\nVocê precisará de {
              coberturalata:.2f} latas de tinta de 18 litros.")
    print(f"Seu orçamento ficou {valortotallata:.2f} Reais.\n")

if escolha == "galao":
    if coberturagalao <= 1:
        print(f"\nVocê precisará de apenas {
              coberturagalao:.2f} galão de tinta de 3.6 litros.")
    else:
        print(f"\nVocê precisará de {
              coberturagalao:.2f} galões de tinta de 3.6 litros.")
    print(f"Seu orçamento ficou {valortotalgalao:.2f} Reais.\n")

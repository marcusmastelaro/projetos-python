# 13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("Digite o Sexo (Valores aceitos: F ou M ): ")

while (sexo not in "MF"):
    print("Valor inválido, digite novamente.")
    sexo = input("\nDigite o Sexo (Valores aceitos: F ou M ): ")

altura = float(input("Digita a altura: "))

if (sexo == "M"):
    pesoidealm = ((72.7 * altura) - 58)
    print(f"\nO peso ideal para este homem é: {pesoidealm:.2f}")
else:
    pesoidealf = ((62.1 * altura) - 44.7)
    print(f"\nO peso ideal para esta mulher é: {pesoidealf:.2f}")

# Escreva um programa que receba 2 valores inteiros referentes à largura e altura de um
# retângulo e imprima na tela um retângulo com essas dimensões.

altura = int(input("Digite a altura do retangulo: "))
largura = int(input("Digite a largura do retangulo: "))

for i in range(0, altura, 1):  # altura 6
    if (i == 0 or i == (altura-1)):
        for j in range(0, largura, 1):  # largura 10
            print("* ", end="")  # foi impresso um asterisco e 1 espaço
        print()
    else:
        for j in range(0, largura, 1):
            if (j == 0 or j == (largura-1)):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

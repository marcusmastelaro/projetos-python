# Faça um Programa que peça um número correspondente a um
# determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("\nDigite o ano desejado: "))
if ano % 4 == 0:
    print("\nEsse ano é bisexto.")
else:
    print("\nEsse não é um ano bisexto")

# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
num3 = float(input("Digite um numero real: "))

calculo1 = (num1*2)*(num2/2)
calculo2 = (num1*3) + num3
calculo3 = num3**3

print(f"\nO resultado do primeiro problema é: ", calculo1)
print(f"\nO resultado do segundo problema é: ", calculo2)
print(f"\nO resultado do terceiro problema é: {calculo3:.2f}")

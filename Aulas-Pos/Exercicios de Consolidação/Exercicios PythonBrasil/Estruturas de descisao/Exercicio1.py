# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
while num1 == num2:
    print("\nNumeros iguais. digite novamente.\n")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(
        f"O primeiro numero digitado é o de maior valor. Seu valor é {num1}.\n")
else:
    print(
        f"O segundo numero digitado é o de maior valor. Seu valor é {num2}.\n")

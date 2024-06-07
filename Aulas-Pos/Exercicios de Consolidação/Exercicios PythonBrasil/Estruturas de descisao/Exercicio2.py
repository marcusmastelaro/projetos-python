# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


valor = input(
    "Digite um número e vamos verificar se ele é positivo ou negativo: ")
while not (valor.replace('.', '', 1).isdigit() or (valor.lstrip('-').replace('.', '', 1).isdigit() and valor.count('-') == 1)):
    print("\nEste valor não é válido. Digite apenas numeros negativos ou positivos.\n")
    valor = input(
        "Digite um número e vamos verificar se ele é positivo ou negativo: ")
valor = float(valor)

if valor >= 0:
    print(f"\nO valor digitado foi {valor}, e ele é positivo.\n")
else:
    print(f"\nO valor digitado foi {valor}, e ele é negativo.\n")

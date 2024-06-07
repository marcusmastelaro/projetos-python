# Escreva um programa que leia o número de um funcionário, seu número de horas
# trabalhadas, o valor que recebe por hora e calcule o salário dele. A seguir, mostre o número e o
# salário do funcionário, com duas casas decimais

func1 = int(input("Digite o código do funcionario 1: "))
horasfunc1 = int(input("Digite as horas trabalhadas no funcionario 1: "))
valorfunc1 = float(input("Digite o valor da hora do funcionario 1: "))
salfunc1 = (horasfunc1 * valorfunc1)

func2 = int(input("\nDigite o código do funcionario 2: "))
horasfunc2 = int(input("Digite as horas trabalhadas no funcionario 2: "))
valorfunc2 = float(input("Digite o valor da hora do funcionario 2: "))
salfunc2 = (horasfunc2 * valorfunc2)

validasal = int(input("\n\nDigite o código do funcionario: "))
if (validasal == func1):
    print(f"O salario do funcionário de código {func1} é: {salfunc1:.2f}")
elif (validasal == func2):
    print(f"O salario do funcionário de código {func2} é: {salfunc2:.2f}")
else:
    print("Funcionario Invalido.")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorhora = float(input("Digite o Valor da sua hora de trabalho: "))
horastrabalhadas = int(
    input("Digite a quantidade de horas trabalhadas no mês: "))
salario = (valorhora * horastrabalhadas)

print(f"\nSeu salário será {salario:.2f}")

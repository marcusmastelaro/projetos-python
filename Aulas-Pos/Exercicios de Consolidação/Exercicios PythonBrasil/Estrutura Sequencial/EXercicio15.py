# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o IR,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valorhora = float(input("Digite o valor da sua hora de trabalho: "))
horastrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
salariobruto = (valorhora * horastrabalhadas)
print(f"\nSeu Salário Bruto esse mes é: {salariobruto:.2f}")

ir = (salariobruto * 0.11)
inss = (salariobruto * 0.08)
sindicato = (salariobruto * 0.05)
totaldescontos = (ir + inss + sindicato)
salarioliquido = (salariobruto - ir - inss - sindicato)

print(f"\nO Valor de IRRF referente a seu salário é: {ir:.2f}")
print(f"O Valor de INSS referente a seu salário é: {inss:.2f}")
print(f"O Valor descontado de seu salário referente ao sindicato é: {
      sindicato:.2f}")
print(f"O Total de descontos em seu salário é: {totaldescontos:.2f}")
print(f"\nSeu salário liquido é: {salarioliquido:.2f}")

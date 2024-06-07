# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


valor_hora = float(input("Digite o valor de sua hora de trabalho: "))
hr_trabalho = int(input("Digite a quantidade de horas trabalhadas no mes: "))

sal_bruto = (valor_hora * hr_trabalho)
fgts = 11
vl_fgts = ((sal_bruto*fgts)/100)
inss = 10
vl_inss = ((sal_bruto*inss)/100)

desc_sindc = 3
vl_desc_sindc = ((sal_bruto*desc_sindc)/100)

if (sal_bruto <= 900):
    vl_desc_ir = 0
    desc_ir = 0
elif (sal_bruto <= 1500):
    desc_ir = 5
    vl_desc_ir = ((sal_bruto*desc_ir)/100)
elif (sal_bruto <= 2500):
    desc_ir = 10
    vl_desc_ir = ((sal_bruto*desc_ir)/100)
else:
    desc_ir = 20
    vl_desc_ir = ((sal_bruto*desc_ir)/100)

tot_desc = (vl_inss + vl_desc_sindc + vl_desc_ir)
sal_liquido = (sal_bruto - vl_desc_ir - vl_desc_sindc)

print(f"\nSalário Bruto: ({valor_hora} * {hr_trabalho}): R${sal_bruto} Reais")
print(f"(-) IR ({desc_ir}%): R${vl_desc_ir} Reais")
print(f"(-) INSS ({inss}%): R${vl_inss} Reais")
print(f"(-) Sindicado ({desc_sindc}%): R${vl_desc_sindc} Reais ")
print(f"FGTS ({fgts}%): R${vl_fgts} Reais")
print(f"Total de descontos: R${tot_desc} Reais")
print(f"Salario Liquido: R${sal_liquido} Reais\n")

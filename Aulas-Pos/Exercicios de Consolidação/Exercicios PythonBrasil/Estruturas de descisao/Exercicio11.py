# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

aumento20 = float(20)
aumento15 = float(15)
aumento10 = float(10)
aumento5 = float(5)


salario_atual = float(input("Digite o salário do colaborador: "))
if salario_atual <= 280:
    salario_novo = (salario_atual + ((salario_atual * aumento20)/100))
    valor_aumento20 = salario_atual * (aumento20/100)
    print(f"\nO Salario atual do colaborador é {salario_atual} Reais.")
    print(f"Ele receberá um aumento de {aumento20}%")
    print(f"O aumento recebido será de {valor_aumento20} Reais.")
    print(f"Seu novo salário será {salario_novo} Reais.")

elif salario_atual <= 700:
    salario_novo = (salario_atual + ((salario_atual * aumento15)/100))
    valor_aumento15 = salario_atual * (aumento15/100)
    print(f"\nO Salario atual do colaborador é {salario_atual} Reais.")
    print(f"Ele receberá um aumento de {aumento15}%")
    print(f"O aumento recebido será de {valor_aumento15} Reais.")
    print(f"Seu novo salário será {salario_novo} Reais.")

elif salario_atual <= 1500:
    salario_novo = (salario_atual + ((salario_atual * aumento10)/100))
    valor_aumento10 = salario_atual * (aumento10/100)
    print(f"\nO Salario atual do colaborador é {salario_atual} Reais.")
    print(f"Ele receberá um aumento de {aumento10}%")
    print(f"O aumento recebido será de {valor_aumento10} Reais.")
    print(f"Seu novo salário será {salario_novo} Reais.")

else:
    salario_novo = (salario_atual + ((salario_atual * aumento5)/100))
    valor_aumento5 = salario_atual * (aumento5/100)
    print(f"\nO Salario atual do colaborador é {salario_atual} Reais.")
    print(f"Ele receberá um aumento de {aumento5}%")
    print(f"O aumento recebido será de {valor_aumento5} Reais.")
    print(f"Seu novo salário será {salario_novo} Reais.")

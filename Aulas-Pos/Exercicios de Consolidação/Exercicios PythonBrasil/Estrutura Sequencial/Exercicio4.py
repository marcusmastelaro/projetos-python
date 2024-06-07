# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a nota do Primeiro Bimestre: "))
nota2 = float(input("Digite a nota do Segundo Bimestre: "))
nota3 = float(input("Digite a nota do Terceiro Bimestre: "))
nota4 = float(input("Digite a nota do Quarto Bimestre: "))

variaveis = [var for var in locals() if var.startswith("nota")]
qtde_variaveis = len(variaveis)

media = (nota1+nota2+nota3+nota4) / qtde_variaveis
print(f"\nA média do aluno é:", media)

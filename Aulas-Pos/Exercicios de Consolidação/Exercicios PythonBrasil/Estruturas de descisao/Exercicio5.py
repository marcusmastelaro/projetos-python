# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nomealuno = input("Digite o nome do Aluno: ")
nota1 = float(input("Digite a Nota 1 do Aluno: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota 1 inválida. Digite a Nota 1 do Aluno: "))

nota2 = float(input("Digite a Nota 2 do Aluno: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota 2 inválida. Digite a Nota 2 do Aluno: "))

nota_final = (nota1 + nota2)/2

if nota_final < 7:
    print(f"\nO Aluno {nomealuno} teve média {nota_final} e foi reprovado.\n")
elif nota_final < 10:
    print(f"\nO Aluno {nomealuno} teve média {nota_final} e foi aprovado.\n")
else:
    print(f"\nO Aluno {nomealuno} teve média {
          nota_final} e foi aprovado com distinção. Parabéns {nomealuno}!!\n")

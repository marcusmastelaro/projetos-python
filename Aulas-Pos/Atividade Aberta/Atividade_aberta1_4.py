nota = int(input("digite uma nota entre 0 e 100: "))

while nota > 100 or nota < 0:
    print("nota invalida!")
    nota = int(input("digite uma nota entre 0 e 100: "))

if nota < 60:
    print("aluno reprovado")
else:
    print("aluno aprovado")
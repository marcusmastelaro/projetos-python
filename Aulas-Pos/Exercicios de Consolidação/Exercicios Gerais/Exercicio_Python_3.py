# ) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule
# a média desse estudante, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem
# peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
print("Calculo de média Ponderada de 3 valores")
pesoa = 2
pesob = 3
pesoc = 5

nota1 = float(input("Nota 1 - Digite uma nota entre 0 e 10: "))
while nota1 > 10 or nota1 < 0:
    print("Nota Invalida. Digite novamente")
    nota1 = float(input("Nota 1 - Digite uma nota entre 0 e 10: "))

nota2 = float(input("\nNota 2 - Digite uma nota entre 0 e 10: "))
while nota2 > 10 or nota2 < 0:
    print("Nota Invalida. Digite novamente")
    nota2 = float(input("Nota 2 - Digite uma nota entre 0 e 10: "))

nota3 = float(input("\nNota 3 - Digite uma nota entre 0 e 10: "))
while nota3 > 10 or nota3 < 0:
    print("Nota Invalida. Digite novamente")
    nota3 = float(input("Nota 3 - Digite uma nota entre 0 e 10: "))

print(f"\nAs notas do Aluno foram :", "Nota 1 ->",
      nota1, " Nota 2 ->", nota2, " Nota 3 ->", nota3)
media = ((nota1 * pesoa) + (nota2 * pesob) +
         (nota3 * pesoc)) / (pesoa + pesob + pesoc)
media = round(media, 1)
print(f"\nA Media do Aluno é: ", media)

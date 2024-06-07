# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de
# um aluno. A seguir, calcule a média dele, sabendo que a nota A tem peso 3.5 e a nota B tem peso
# 7.5 (A soma dos pesos, portanto, é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com
# uma casa decimal.


print("Vamos receber as notas dos alunos")
PesoA = 3.5  # Essa nota tem peso de 3.5
PesoB = 7.5  # Essa nota tem peso de 7.5
NotaA = float(input("Imprima a primeira nota do Aluno: "))
NotaB = float(input("Imprima a segunda nota do Aluno: "))

# Calculando a média das notas
Media = ((NotaA * PesoA) + (NotaB * PesoB)) / (PesoA + PesoB)
Media = round(Media, 1)
print(f"A média do Aluno é: ", Media)

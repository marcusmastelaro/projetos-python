import numpy as np
notas = np.zeros(5, dtype=float)
print("O vetor atual é: ", notas)

for i in range (0,5):
    notas[i] = float(input("\nDigite a nota %d do aluno: " % (i+1)))
    print("Nota %d Registrada" % (i+1))
media_final = 0
for i in range(0,5):
    media_final = media_final + notas[i]
media_final = media_final / 5

if media_final >= 60:
    print("\nAluno aprovado com média %.2f!" % media_final)
else:
    print("\nAluno reprovado com média %.2f" % media_final)
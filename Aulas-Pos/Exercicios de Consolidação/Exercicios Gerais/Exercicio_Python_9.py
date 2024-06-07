# Faça um programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram  lidas. Imprima as consoantes

# import numpy as np
# string = input("Digite uma string contendo 10 caracteres: ")
# contstring = 0
# if len(string) != 10:
#     print("Você não digitou 10 caracteres;")
# else:
#     string = string.lower()
#     for consoante in string:
#         if (consoante not in "aeiou"):
#             contstring += 1
# print("Dentre os caracteres que você digitou há %d consoantes" % (contstring))

contastring = 0
string = input("Digite uma string contendo 10 caracteres: ")
while len(string) != 10:
    string = input("Você não digitou 10 caracteres, digite novamente: ")

string = string.lower()
for consoante in string:
    if (consoante not in "aeiou"):
        contastring += 1
if contastring == 1:
    print("Dentre os caracteres que você digitou há %d consoante" % (contastring))
else:
    print("Dentre os caracteres que você digitou há %d consoantes" % (contastring))

# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo. (F ou M): ")
sexo = sexo.lower()
while sexo not in ("f", "m"):
    sexo = input("Sexo inválido. Digite o sexo. (F ou M): ")
    sexo = sexo.lower()
if sexo == "f":
    print(f"O Sexo informado é F - Feminino")
else:
    print(f"O Sexo informado é M - Masculino")

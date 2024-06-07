a = "Diga Olá!"
print("Caractere de Indice 1...")
print(a[1]) #acessa o elemento do string
print()

#percorre o elemento do string 1 a 1
print("Imprime String...")
for x in a:
    print(x, end="")
print("\n")

#percorre string com passo 2
print("Imprime String...")
for i in range(0, len(a), 2):
    print(a[i], end="")
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def apenas_um_char():
    while True:
        letra = input("\nDigite uma letra apenas: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Por favor. Digite apenas uma letra: ")


caractere = apenas_um_char()

if caractere in "aeiou":
    print(f"\nA letra {caractere} é uma vogal.\n")
else:
    print(f"\nA letra {caractere} é uma consoante.\n")

import numpy as np
def funcao_string(carac, str, tam):
    string = ""
    for i in range(0,tam):
        if(i + 1) % 2 == 0:
            string  += carac
        else:
            string += str[i]
    return string

substitui_caractere = input("Insira o caractere substituto: ")
print(f"O caractere substituto é:", substitui_caractere)
insere_string = input("\nInsira sua string: ")
print(f"sua string atual é:", insere_string)
tamanho_string = len(insere_string)
print(f"O tamanho da string é:", tamanho_string)
string = funcao_string(substitui_caractere,insere_string,tamanho_string)
print(f"\nSua nova String é:", string)


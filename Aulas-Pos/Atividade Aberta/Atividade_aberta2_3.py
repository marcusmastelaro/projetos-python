#Crie uma função que receba dois inteiros ent1 e ent2 . 
#Essa função deve imprimir todos os textos quando a condição for atendida
#- “ent1 - ent2 é negativo”, condição: caso ent1 menos ent2 seja menor que zero,
#- “ent1 * ent2 é negativo”, condição: caso ent1 multiplicado por ent2 seja menor que zero,
#- “ent1 + ent2 é negativo”, condição: caso ent1 somado a ent2 seja menor que zero.

def numeros_inteiros(ent1, ent2):
    if ent1 - ent2 < 0:
        print(f"\n{ent1} - {ent2} =", ent1 - ent2, "---> O Resultado é negativo.\n")
    if ent1 * ent2 < 0:
        print(f"\n{ent1} * {ent2} =", ent1 * ent2, "---> O Resultado é negativo.\n")
    if ent1 + ent2 < 0:
        print(f"\n{ent1} + {ent2} =", ent1 + ent2, "---> O Resultado é negativo.\n")

ent1 = int(input("\nDigite o primeiro numero: "))
ent2 = int(input("Digite o segundo numero: "))
numeros_inteiros(ent1,ent2)
#  Faça uma função que retorne o fatorial de um número N maior que 0. Agora, refaça o
# problema proposto de modo recursivo.

# calcula fatorial de numero>0
def meu_fatorial(n):  # 6
    fatorial = 1
    for i in range(n, 1, -1):
        print(i)
        fatorial = fatorial * i
    return fatorial

# calcula fatorial de numero>0 recursivamente


def meu_fatorial_rec(n):
    if (n == 1):
        return 1
    else:
        return n*meu_fatorial_rec(n-1)


# programa principal
n = int(input("Informe um número do qual deseja calcular o fatorial: "))

print("Fatorial calculado sem recursão: ", meu_fatorial(n))
print("Fatorial calculado com recursão: ", meu_fatorial_rec(n))

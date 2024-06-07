#  Faça uma função que retorne a soma dos N primeiros números da sequência de Fibonacci.

import pdb
# pdb.set_trace()

# funcao somaFibonacci


def somaFibonacci(n):
    n0 = soma = 0
    n1 = 1
    if (n == 0):
        return n0
    else:
        for i in range(2, n+1, 1):
            soma += n1
            temp = n1
            n1 = n1 + n0
            n0 = temp
            # print(n1)
            # pdb.set_trace()
        return soma


# programa principal
n = int(input("Informe n, e retornarei a soma dos n primeiros números da sequência de Fibonacci: "))
resultado = somaFibonacci(n)
print("A soma dos %d números de Fibonacci é %d" % (n, resultado))

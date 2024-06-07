#  Leia um número inteiro n maior ou igual à 100 e menor ou igual à 999. Imprima,
# separadamente, os dígitos que representam as unidades, dezenas e centenas do número.

n = int(input("Digite um numero entre 100 e 999: "))
while n < 100 or n > 999:
    print("Número inválido. Digite novamente")
    n = int(input("Digite um numero entre 100 e 999: "))

unidades = n % 10
print(n)
print(unidades)


n = n // 10  # divisao inteira
dezenas = n % 10
print(n)
print(dezenas)

n = n // 10
centenas = n % 10
print(n)
print(centenas)

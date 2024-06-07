#  Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de
# A e B pelo produto de C e D segundo a fórmula: DIFERENCA= (A * B - C * D).

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))
print(f"O valor de A é:", a)
print(f"O valor de B é:", b)
print(f"O valor de C é:", c)
print(f"O valor de D é:", d)


calculoab = (a * b)
print(f"\nO Produto de A e B é:", calculoab)
calculocd = (c * d)
print(f"\nO Produto de C e D é:", calculocd)

diferenca = (calculoab - calculocd)
print(f"\nA diferença é:", diferenca)

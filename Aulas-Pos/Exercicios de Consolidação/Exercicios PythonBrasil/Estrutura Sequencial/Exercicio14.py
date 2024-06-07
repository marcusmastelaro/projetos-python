#  14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

limite = 50
multakg = 4

peso = float(input("Digite o peso do peixe: "))

excesso = peso - limite
valordamulta = excesso * multakg

if peso <= limite:
    valordamulta = 0
    print(f"\nLimite de pesca aceito: {limite:.2f} kgs")
    print(f"Seu pescado tem {
          peso:.2f} kg, e por isso você não tem multa por excesso de peso a pagar.")
else:
    print(f"\nLimite de pesca aceito: {limite:.2f} kgs")
    print(f"Seu pescado possui {peso:.2f} kgs. São {
          excesso:.2f} kgs acima do limite aceito.")
    print(f"Você precisará pagar uma multa de {valordamulta:.2f} Reais.")

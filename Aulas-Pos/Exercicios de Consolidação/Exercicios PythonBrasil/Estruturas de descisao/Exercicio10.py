# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input(
    "Digite em que turno você estuda. Digite M para Matutino, V para Vespertino ou N para Noturno): ").lower()
while turno not in ("mvn"):
    turno = input(
        "Turno inválido. Digite M para Matutino, V para Verspetino ou N para Noturno: ").lower()
if turno == "m":
    print(f"Bom dia!!")
elif turno == "v":
    print(f"Boa tarde!!")
else:
    print(f"Boa Noite!!")

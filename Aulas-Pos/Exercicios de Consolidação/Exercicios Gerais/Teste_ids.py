# abrindo o arquivo de vendas
with open("lista_ids.txt", "r") as arquivo:
    lista = arquivo.read()
lista_linha = (lista.split("\n"))
# lista_linha = [int(valor) for valor in lista_linha]
# lista_linha = lista_linha[1:]

with open("nova_lista_ids.txt", "w") as novo_arquivo:
    for valor in lista_linha:
        novo_arquivo.write(str(valor) + ",\n")

print("Lista salva com sucesso no arquivo nova_lista_ids.txt")

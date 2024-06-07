#abrindo o arquivo de vendas
with open("vendasloja.txt", "r") as arquivo:
    #adicionando os dados no arquivo na variavel "Relatorio"
    relatorio = arquivo.read()
    #separa os registros após cada "Enter"
relatorio_linha = (relatorio.split("\n"))
# print(relatorio_linha)
#agora preciso somar tudo o que vier após o ponto e virgula para cada linha do relatorio e excluir a primeira linha do relatorio que são os cabeçalhos
relatorio_linha = relatorio_linha[1:]

faturamento = 0
#aqui inicio o laço for definindo a variavel linha como variavel do meu relatorio
for linha in relatorio_linha:
    #aqui eu crio uma variavel chamada posicao_pv e encontro em qual posição está o ponto e virgula
    #pois meu valor é o que vem logo após o ponto e virgula
    #posicao_pv = linha.find(";")
    valor = float(linha.split(";")[-1])
    # print(valor)
    #aqui estou falando que meu valor é a posicao_pv + 1 até o final, representado pelos dois pontos
    # valor = float(linha[posicao_pv+1 :])
    #aqui falo que meu novo valor de faturameto é o que faturamento tinha antes (0) + o valor encontrado
    #vale ressaltar que essa parte precisa estar dentro do for para que ele pegue todos os valores.
    #caso esteja fora, vai pegar apenas o ultimo valor da lista
    faturamento += valor
print('Valor: %s' % faturamento)

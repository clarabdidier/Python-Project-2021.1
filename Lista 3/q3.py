dados = input()
dadosdict = dict()
i = 0
soma_produto = 0
multi_produto = 0

while dados != '*':
    dadoslista = dados.split(',')
    dadosdict[dadoslista[0]] = dadoslista[1]
    dados = input()

qtd_tiposalimento = int(input())
while qtd_tiposalimento != 0:
    if 1 <= qtd_tiposalimento <= 100:
        while i < qtd_tiposalimento:
            qtdenome = input()
            lista_qtdenome = qtdenome.split()
            y = lista_qtdenome[1:]
            y = " ".join(y)
            lista_qtdenome = [lista_qtdenome[0], y]
            if lista_qtdenome[1] in dadosdict:
                multi_produto = int(dadosdict[lista_qtdenome[1]]) * int(lista_qtdenome[0])
                soma_produto = soma_produto + multi_produto
            i += 1

        if soma_produto > 130:
            diferenca = soma_produto - 130
            print("Menos", diferenca, "mg")
        if 110 <= soma_produto <= 130:
            print(soma_produto, "mg")
        if soma_produto < 110:
            diferenca1 = 110 - soma_produto
            print('Mais', diferenca1, 'mg')
    i = 0
    soma_produto = 0
    multi_produto = 0
    qtd_tiposalimento = int(input())

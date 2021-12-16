codigo_acao = input()
acoes = dict()

while codigo_acao != 'fim':
    nome_acao = input()
    valor_acao = float(input())
    qtd_acao = int(input())
    dados_acoes = list()
    historico = list()
    historico.append(valor_acao)
    dados_acoes.append(nome_acao)
    dados_acoes.append(valor_acao)
    dados_acoes.append(qtd_acao)
    dados_acoes.append(historico)
    acoes[codigo_acao] = dados_acoes
    codigo_acao = input()


codigo_acao = input()
while codigo_acao != 'fim':
    valor_atual = float(input())
    acao = acoes[codigo_acao]
    acoes[codigo_acao][3].append(valor_atual)

    historico10 = historico[-10:]
    media_historico = sum(historico10) / len(historico10)

    if valor_atual > acoes[codigo_acao][1] or valor_atual > media_historico:
        print('Venda')
    else:
        print('Compra')
    acoes[codigo_acao][1] = valor_atual
    codigo_acao = input()




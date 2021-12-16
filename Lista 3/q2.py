dados = input()
codigo_valor = dict()
codigo_pontos = dict()

while dados != '*':
    dados = dados.split()
    codigo_valor[dados[0]] = dados[1]
    codigo_pontos[dados[0]] = dados[2]
    dados = input()

placas_multas = input()
placas = list()
multas = list()
while placas_multas != '*':
    placas_multas = placas_multas.split()
    placas.append(placas_multas[0])
    multas.append(placas_multas[1:])
    placas_multas = input()

i = 0
j = 0
k = 0
preco_total = 0
soma_pontos = 0
placa_valor = dict()
placa_pontos = dict()
while i < len(multas):
    preco_total = 0
    soma_pontos = 0
    while j < len(multas[i]):
        preco_total += float(codigo_valor[multas[i][j]])
        placa_valor[placas[i]] = preco_total
        j += 1
    while k < len(multas[i]):
        soma_pontos += float(codigo_pontos[multas[i][k]])
        placa_pontos[placas[i]] = soma_pontos
        k += 1
    k = 0
    j = 0
    i += 1

i = 0
while i < len(placas):
    placas.sort()
    print(placas[i], '{:.2f}'.format(placa_valor[placas[i]]), int(placa_pontos[placas[i]]))
    i += 1
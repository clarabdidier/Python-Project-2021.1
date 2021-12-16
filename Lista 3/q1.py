produtos = int(input())
i = 0
cardapio = dict()
precototal = 0

while i < produtos:
    codigo = int(input())
    nome = input()
    preco = float(input())
    cardapio[codigo] = preco
    i = i + 1

codigocliente = int(input())

while codigocliente != 0:
    qtd = int(input())
    if codigocliente in cardapio:
        if qtd > 0:
            precocliente = cardapio[codigocliente] * qtd
            precototal += precocliente
    codigocliente = int(input())

print('{:.2f}'.format(precototal))

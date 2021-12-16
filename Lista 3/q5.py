nome_valor = input()
nomes_valores = dict()
listanomes = list()
while nome_valor != '*':
    nomes = nome_valor.split()
    y = nomes[:-1]
    y = ' '.join(y)
    listanomes.append(y)
    nomes_valores[y] = nomes[-1]
    nome_valor = input()

comando = input()
while comando != 'total':
    if 'retire' in comando:
        x = comando[7:]
        del nomes_valores[x]
        listanomes.remove(x)

    if 'quantidade' in comando:
        print(len(nomes_valores))
    comando = input()

i = 0
preco_total = 0
while i < len(nomes_valores):
    preco_total += float(nomes_valores[listanomes[i]])
    i = i + 1
print('{:.2f}'.format(preco_total))

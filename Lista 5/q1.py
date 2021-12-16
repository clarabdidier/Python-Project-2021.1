qtd = input()
valor_doado = int(input())
qtd_produtos = qtd.split(',')

precos = (5.50, 6.00, 7.50, 1.99, 4.00, 6.70, 1.20, 2.80, 5.30, 5.00, 3.00, 2.00, 3.50, 0.80, 1.00, 0.80, 5.40, 1.90, 5.00, 10.00, 0.50, 0.50, 5.00, 4.50, 1.99, 2.90, 0.30)

soma_produtos = 0
i = 0
while i < len(precos):
    preco_produto = int(qtd_produtos[i]) * float(precos[i])
    soma_produtos += preco_produto
    i = i + 1

num_cestas = int(valor_doado / soma_produtos)

print(f'O valor da cesta basica ficou em:', 'R${:.2f}'.format(soma_produtos))
print(f'Com o valor doado pode ser comprada {num_cestas} cestas basicas')
qtd_palavras = int(input())
i = 0
j = 0
g = 0
soma_pesos = 0
dictpalavras = dict()
palavrasprocuradas = list()

while i < qtd_palavras:
    palavradeatt = input()
    palavradeatt = palavradeatt.upper()
    palavraepeso = palavradeatt.split()
    palavrasprocuradas.append(palavraepeso[0])
    dictpalavras[palavraepeso[0]] = float(palavraepeso[1])
    i = i + 1

k = float(input())

counts = dict()
texto = input()
texto = texto.upper()
texto = texto.replace('.', ' ')
texto = texto.replace(',', ' ')
palavras = texto.split()
for palavra in palavras:
    counts[palavra] = counts.get(palavra, 0) + 1

while j < len(palavrasprocuradas):
    if palavrasprocuradas[j] in palavras:
        soma_pesos += dictpalavras[palavrasprocuradas[j]] * counts[palavrasprocuradas[j]]
    j = j + 1
while g < len(palavrasprocuradas):
    if palavrasprocuradas[g] in palavras:
        print(palavrasprocuradas[g] , counts[palavrasprocuradas[g]])
    g = g + 1


if soma_pesos > k:
    print('SIM')
else:
    print('NAO')


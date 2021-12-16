palavras_proibidas = input()
palavras_proibidas = palavras_proibidas.upper()
palavras_proibidas = palavras_proibidas.split()
palavras_proibidas.sort()

texto = input()
texto_inteiro = str()
while texto != 'FIM':
    texto_inteiro = texto_inteiro + ' ' + texto
    texto = input()

counts = dict()
texto_inteiro = texto_inteiro.upper()
texto_inteiro = texto_inteiro.replace('.', ' ')
texto_inteiro = texto_inteiro.replace(',', ' ')
palavras = texto_inteiro.split()

for palavra in palavras:
    counts[palavra] = counts.get(palavra, 0) + 1

i = 0
while i < len(palavras_proibidas):
    if palavras_proibidas[i] in counts:
        print(palavras_proibidas[i], counts[palavras_proibidas[i]])
    i = i + 1

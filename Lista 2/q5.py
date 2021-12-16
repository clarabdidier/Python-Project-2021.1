num = int(input())
i = 0
j = 0
frases = list()

while i < num:
    frase = input()
    frases.append(frase)
    i = i + 1

frases = ''.join(frases)
frases = list(frases)

letras = input()
letras = list(letras)
while j < len(letras):
    print(letras[j], "=", frases.count(letras[j]))
    j = j + 1

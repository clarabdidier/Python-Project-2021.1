frase = input()
frase = frase.lower()
anagrama = input()
anagrama = anagrama.lower()

frase = frase.replace('.', '')
frase = frase.replace(',', '')
frase = frase.replace('!', '')
frase = frase.replace('?', '')
frase = frase.replace(' ', '')
anagrama = anagrama.replace('.', '')
anagrama = anagrama.replace(',', '')
anagrama = anagrama.replace('!', '')
anagrama = anagrama.replace('?', '')
anagrama =anagrama.replace(' ', '')

listafrase = list(frase)
listaanagrama = list(anagrama)


listafrase = sorted(listafrase)
listaanagrama = sorted(listaanagrama)

if listafrase == listaanagrama:
    print('True')
else:
    print('False')
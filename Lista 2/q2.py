while True:
    frase = input()
    frase = frase.upper()
    frase = frase.replace('3', 'E')
    frase = frase.replace('4', 'A')
    frase = frase.replace('1', 'I')
    frase = frase.replace('5', 'S')

    if (frase == 'FIM' or frase == 'SAIR'):
        break
    else:
        print(frase)
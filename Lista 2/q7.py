while True:
    nome = input()
    nome = nome.title()
    nome = nome.split()

    if "Da" in nome:
        min = nome.index('Da')
        nome[min] = 'da'
    if "De" in nome:
        min = nome.index('De')
        nome[min] = 'de'
    if "Di" in nome:
        min = nome.index('Di')
        nome[min] = 'di'
    if "Do" in nome:
        min = nome.index('Do')
        nome[min] = 'do'
    if "Du" in nome:
        min = nome.index('Du')
        nome[min] = 'du'
    if "E" in nome:
        min = nome.index('E')
        nome[min] = 'e'

    nome = ' '.join(nome)

    if nome != '*':
        print(nome)
    if nome == '*':
        break
while True:
    email = input()
    if email == 'sair':
        break
    email = email.lower()
    arroba = email.find('@')
    posarroba = email[arroba+1:]
    dominio = posarroba.split('.')

    if email[0] == '@':
        print('errado')
    elif posarroba[0] == '.':
        print("errado")
    elif len(dominio) != 3:
        print("errado")
    elif dominio[0] == '':
        print('errado')
    elif dominio[1] == '':
        print("errado")
    elif dominio[2] == '':
        print("errado")
    else:
        print("certo")
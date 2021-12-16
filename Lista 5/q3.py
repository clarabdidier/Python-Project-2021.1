dados = input().upper()
i = 0
lista_mesa1 = list()
lista_mesa2 = list()
lista_mesa3 = list()
lista_mesa4 = list()

if dados == '-1':
    print('JANTAR SEM CONVIDADOS')
else:
    while 0 <= i < 10 and dados != '-1':
        lista_dados = dados.split()
        nome = lista_dados[0]
        idade = lista_dados[1]
        time = lista_dados[2]

        if int(idade) > 30 and (time == 'FLAMENGO' or time == 'SPORT' or time == 'VITORIA'):
            lista_mesa1.append(nome)
        elif 18 <= int(idade) <= 36 and (time == 'VASCO' or time == 'TREZE' or time == 'SANTOS'):
            lista_mesa2.append(nome)
        elif 10 <= int(idade) <= 18 and (time == 'BAHIA' or time == 'FORTALEZA' or time == 'GREMIO'):
            lista_mesa3.append(nome)
        else:
            lista_mesa4.append(nome)
        i = i + 1
        
        if i <= 9:
            dados = input().upper()
        

    print('MESA 1')
    if len(lista_mesa1) == 0:
        print('VAZIA')
    else:
        j = 0
        k = 0
        while k < len(lista_mesa1):
            k = k + 1
            print(k, lista_mesa1[j])
            j = j + 1
    print('\nMESA 2')
    if len(lista_mesa2) == 0:
        print('VAZIA')
    else:
        j = 0
        k = 0
        while k < len(lista_mesa2):
            k = k + 1
            print(k, lista_mesa2[j])
            j = j + 1
    print('\nMESA 3')
    if len(lista_mesa3) == 0:
        print('VAZIA')
    else:
        j = 0
        k = 0
        while k < len(lista_mesa3):
            k = k + 1
            print(k, lista_mesa3[j])
            j = j + 1
    print('\nMESA 4')
    if len(lista_mesa4) == 0:
        print('VAZIA')
    else:
        j = 0
        k = 0
        while k < len(lista_mesa4):
            k = k + 1
            print(k, lista_mesa4[j])
            j = j + 1
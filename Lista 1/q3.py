soma_veiculos = 0
soma_acidentes = 0
soma_fatais = 0
soma_naofatais = 0
soma_semvitimas = 0
soma_acidentes_municipio = 0
maior_numacidentes = 0
menor_numacidentes = 9999999
maior_nome = str
menor_nome = str
lista_nomes = list()
lista_veiculos = list()
lista_acidentesfatais = list()
lista_acidentesnaofatais = list()
lista_acidentessemvitima = list()
maior_ivt = 0
menor_ivt = 999999
maior_nome_ivt = str
menor_nome_ivt = str
maiorivt_veiculos = 0
menorivt_veiculos = 0
maiorivt_fatais = 0
menorivt_fatais = 0
maiorivt_naofatais = 0
menorivt_naofatais = 0
maiorivt_svit = 0
menorivt_svit = 0


i = 0

while True:
    i = i + 1
    nome = str(input(""))
    lista_nomes.append(nome)
    total_veiculos = int(input(""))
    lista_veiculos.append(total_veiculos)
    total_acidentes_fatais = int(input(""))
    lista_acidentesfatais.append(total_acidentes_fatais)
    total_acidentes_naofatais = int(input(""))
    lista_acidentesnaofatais.append(total_acidentes_naofatais)
    total_acidentes_semvitima = int(input(""))
    lista_acidentessemvitima.append(total_acidentes_semvitima)

    ivt = ((5 * total_acidentes_fatais) + (3 * total_acidentes_naofatais) + total_acidentes_semvitima) / total_veiculos

    soma_veiculos = soma_veiculos + total_veiculos
    soma_acidentes = soma_acidentes + total_acidentes_fatais + total_acidentes_naofatais + total_acidentes_semvitima
    soma_fatais = soma_fatais + total_acidentes_fatais
    soma_naofatais = soma_naofatais + total_acidentes_naofatais
    soma_semvitimas = soma_semvitimas + total_acidentes_semvitima
    soma_acidentes_municipio = total_acidentes_fatais + total_acidentes_naofatais + total_acidentes_semvitima

    if soma_acidentes_municipio > maior_numacidentes:
        maior_numacidentes = soma_acidentes_municipio
        maior_nome = nome

    if soma_acidentes_municipio < menor_numacidentes:
        menor_numacidentes = soma_acidentes_municipio
        menor_nome = nome

    if ivt > maior_ivt:
        maior_ivt = ivt
        maior_nome_ivt = nome
        maiorivt_veiculos = total_veiculos
        maiorivt_fatais = total_acidentes_fatais
        maiorivt_naofatais = total_acidentes_naofatais
        maiorivt_svit = total_acidentes_semvitima

    if ivt < menor_ivt:
        menor_ivt = ivt
        menor_nome_ivt = nome
        menorivt_veiculos = total_veiculos
        menorivt_fatais = total_acidentes_fatais
        menorivt_naofatais = total_acidentes_naofatais
        menorivt_svit = total_acidentes_semvitima

    novo = str(input(""))
    if novo == 'S':
        continue
    if novo == 'N':
        break

#4A
print("\n4.a) A quantidade de veiculos no pais:", soma_veiculos)
#4B
print("4.b) A quantidade de acidentes no pais:", soma_acidentes)
#4C
print("4.c) A quantidade de acidentes com vitimas fatais no pais:", soma_fatais)
#4D
print(f"4.d) O municipio com maior numero de acidentes: {maior_nome} ({maior_numacidentes})")
print(f"4.d) O municipio com menor numero de acidentes: {menor_nome} ({menor_numacidentes})")

#5A
media_veiculos = soma_veiculos / i
print('\n5.a) A media de veiculos por municipios:', media_veiculos)
#5B
media_fatais = soma_fatais / i
media_naofatais = soma_naofatais / i
media_semvitimas = soma_semvitimas / i
print('5.b) A media de acidentes com vitimas fatais por municipios:', media_fatais)
print('5.b) A media de acidentes com vitimas nao-fatais por municipios:', media_naofatais)
print('5.b) A media de acidentes sem vitimas por municipios:', media_semvitimas)

#5 C e D
print(f"\n5.c) O maior IVT eh de {maior_ivt} e pertence ao municipio", maior_nome_ivt)
print('5.d) Nome do municipio:', maior_nome_ivt)
print(f'5.d) Quantidade de veiculos de {maior_nome_ivt}:', maiorivt_veiculos)
print(f'5.d) Total de acidentes com vitimas fatais em {maior_nome_ivt}:', maiorivt_fatais)
print(f'5.d) Total de acidentes com vitimas nao-fatais em {maior_nome_ivt}:', maiorivt_naofatais)
print(f'5.d) Total de acidentes sem vitimas em {maior_nome_ivt}:', maiorivt_svit)

print(f"\n5.c) O menor IVT eh de {menor_ivt} e pertence ao municipio", menor_nome_ivt)
print('5.d) Nome do municipio:', menor_nome_ivt)
print(f'5.d) Quantidade de veiculos de {menor_nome_ivt}:', menorivt_veiculos)
print(f'5.d) Total de acidentes com vitimas fatais em {menor_nome_ivt}:', menorivt_fatais)
print(f'5.d) Total de acidentes com vitimas nao-fatais em {menor_nome_ivt}:', menorivt_naofatais)
print(f'5.d) Total de acidentes sem vitimas em {menor_nome_ivt}:', menorivt_svit)

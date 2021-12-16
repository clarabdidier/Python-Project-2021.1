n = float(input())
i = 0
somanl = 0

if 0 <= n <= 10:
    l_qtd = int(input())
    while i < l_qtd:
        if l_qtd > 0:
            nl = float(input())
            if 0 <= nl <= 10:
                somanl = somanl + nl
        i = i + 1

notafinal = float((n * 0.7) + ((somanl / l_qtd) * 0.3))

print('{:.2f}'.format(notafinal))

if 0 <= notafinal < 3:
    print('RED ZONE!')
if 3 <= notafinal < 5:
    print('DA PARA RECUPERAR!')
if 5 <= notafinal < 7:
    print('QUASE LA!')
if 7 <= notafinal < 9:
    print('TA FAVORAVEL!')
if notafinal >= 9:
    print('EXCELENTE!')





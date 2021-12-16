num_criancas = int(input())

if num_criancas <= 0:
    print("Informe um numero positivo")
    exit()

contador = 0
num_meninas = 0
num_meninos = 0
menos_24meses = 0
while contador < num_criancas:
    contador = contador + 1
    sexo = str(input())
    if sexo == 'M':
        num_meninos = num_meninos + 1
    if sexo == 'F':
        num_meninas = num_meninas + 1
    tempo_vida = int(input())
    if tempo_vida <= 24:
        menos_24meses = menos_24meses + 1

print(f"a) {(num_meninas / num_criancas) * 100}% das criancas eram do sexo feminino.")
print(f"b) {(num_meninos / num_criancas) * 100}% das criancas eram do sexo masculino.")
print(f"c) {(menos_24meses / num_criancas) * 100}% das criancas viveram 24 meses ou menos.")
PESO_QUEIJO = 100
PESO_PRESUNTO = 50
PESO_CARNE = 100

num_sanduiches = int(input())

qtd_queijo = (num_sanduiches * PESO_QUEIJO) / 1000
qtd_presunto = (num_sanduiches * PESO_PRESUNTO) / 1000
qtd_carne = (num_sanduiches * PESO_CARNE) / 1000

print(qtd_queijo, "kg de queijo")
print(qtd_presunto, "kg de presunto")
print(qtd_carne, "kg de carne")

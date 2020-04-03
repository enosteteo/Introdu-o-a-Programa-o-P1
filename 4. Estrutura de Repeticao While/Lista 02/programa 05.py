idadeMin = 3
idadeMax = 6
qtde = 0
fim = False

while not fim:
    idade = int(input("-1 para finalizar: "))
    if idadeMax >= idade >= idadeMin:
        qtde += 1
    if idade == -1:
        fim = True
print(qtde)


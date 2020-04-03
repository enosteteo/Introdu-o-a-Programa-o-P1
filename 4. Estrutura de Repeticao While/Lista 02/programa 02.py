cont = 25
qtdeParEPositivo = 0
while cont > 0:
    numero = int(input())
    if (numero >= 0) and (numero % 2 == 0):
        qtdeParEPositivo += 1
    cont -= 1
print(qtdeParEPositivo)

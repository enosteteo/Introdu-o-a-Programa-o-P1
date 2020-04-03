
qtdeFilhos = 0
qtdeFuncionarios = 0
fim = False
while not fim:
    qtde = int(input())
    if qtde < 0:
        fim = True
        break
    qtdeFilhos += qtde
    qtdeFuncionarios += 1


qtdeMedia = qtdeFilhos / qtdeFuncionarios
print(qtdeMedia)
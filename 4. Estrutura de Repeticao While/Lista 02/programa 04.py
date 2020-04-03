fim = 100
qtdeNumPar = 0
soma = 0
cont = 0

while cont != fim:
    num = int(input())
    if num == fim:
        cont = num
        break
    if num % 2 == 0:
        soma += num
        qtdeNumPar += 1
if qtdeNumPar > 0:
    media = soma / qtdeNumPar
    print(media)
else:
    print("Não foram lidos números pares")

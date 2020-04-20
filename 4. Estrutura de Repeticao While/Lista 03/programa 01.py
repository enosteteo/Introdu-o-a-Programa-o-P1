idadeMin = 11
idadeMax = 60
qtde = 0
fim = ""
while fim != "não":
    idade = int(input())
    if idadeMin >= idade or idade > idadeMax:
        qtde += 1
    fim = str.lower(input())
print(qtde)

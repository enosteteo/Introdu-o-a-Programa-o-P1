# Quest 01

terno = "terno"
simples = 120.4
completo = 150.35
fraque = 180.7

acessorio = "acessório"
gravata = 30
sapato = 80
cinto = 15

preco = 0
desconto = 7/100

tipoItem = str.lower(input("Tipo de item: "))
tipoDescrição = str.lower(input("Descrição: "))
if (tipoItem == terno):
    if (tipoDescrição == "simples"):
        preco = simples
    elif (tipoDescrição == "completo"):
        preco = completo
    else:
        preco = fraque
    precoDesc = preco * desconto
    preco = preco - precoDesc
elif (tipoItem == acessorio):
    if (tipoDescrição == "gravata"):
        preco = gravata
    elif (tipoDescrição == "sapato"):
        preco = sapato
    else:
        preco = cinto
print("%.2f" % preco)


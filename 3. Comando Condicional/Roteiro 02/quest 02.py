# Quest 02

jornal = [["mural", 200], ["o coreto", 235]]
revista = [["meu lar", 180], ["sua mesa", 230]]
desconto = 10 / 100
preco = 0.0

item = str.lower(input("item desejado: "))
duracaoAssinatura = int(input("Duração em anos: "))

if (item == jornal[0][0]):
    preco = duracaoAssinatura * jornal[0][1]
elif (item == jornal[1][0]):
    preco = duracaoAssinatura * jornal[1][1]
if (item == revista[0][0]):
    preco = duracaoAssinatura * revista[0][1]
    precoDesc = preco * desconto
    preco = preco - precoDesc
elif (item == revista[1][0]):
    preco = duracaoAssinatura * revista[1][1]
    precoDesc = preco * desconto
    preco = preco - precoDesc

print("%.2f" % preco)


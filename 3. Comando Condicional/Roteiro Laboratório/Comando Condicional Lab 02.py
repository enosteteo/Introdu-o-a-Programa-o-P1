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

# Quest 03

conceitoA = 1 / 8
conceitoB = 1 / 12
conceitoC = 1 / 18
conceitoD = 1 / 18

quantLivros = int(input("Quantidade de livros: "))
quantAlunos = int(input("Quantidade de alunos: "))
conceito = quantLivros / quantAlunos

if conceito < conceitoD:
    print("D")
elif conceito <= conceitoC:
    print("C")
elif conceito <= conceitoB:
    print("B")
else:
    print("A")

# Quest 04

garantiaUm = 3 / 100
garantiaDois = 5 / 100

valorProduto = float(input("Qual o valor do produto? "))
tempoGarantia = int(input("Garantia de quanto tempo? "))

if (tempoGarantia == 1):
    preco = valorProduto * garantiaUm
    valorProduto = valorProduto + preco
elif (tempoGarantia == 2):
    preco = valorProduto * garantiaDois
    valorProduto = valorProduto + preco
print("%.2f" % valorProduto)

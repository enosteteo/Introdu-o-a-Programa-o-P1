# Quest 01

bebida = [["café", 2.50], ["suco", 3.50], ["refrigerante", 4.05]]
ganhaBolo = 3

tipoBebida = str.lower(input("Qual o tipo da bebida? "))
quant = int(input("Quantas? "))
precoTotal = 0
bolo = False

if (tipoBebida == bebida[0][0]):
    precoTotal = quant * bebida[0][1]
elif (tipoBebida == bebida[1][0]):
    precoTotal = quant * bebida[1][1]
    bolo = True
elif (tipoBebida == bebida[2][0]):
    precoTotal = quant * bebida[2][1]

print("%.2f" % precoTotal)

if ((quant >= ganhaBolo) and (bolo == True)):
    print("Ganha bolo")
else:
    print("Não ganha bolo")

# Quest 02

itens = [["bolsa", ["couro", 180], ["tecido", 100]],
         ["relógio", ["metal", 215], ["couro", 150]]]

bolsaCouro = 180
bolsaTecido = 100
relogioMetal = 215
relogioCouro = 150
brinde = "relógio"
preco = 0

presenteEscolhido = str.lower(input("Qual o presente escolhido? "))
tipoEscolhido = str.lower(input("Qual o tipo escolhido? "))

if (presenteEscolhido == "bolsa"):
    if (tipoEscolhido == "couro"):
        print(bolsaCouro)
    elif (tipoEscolhido == "tecido"):
        print(bolsaTecido)
elif (presenteEscolhido == "relógio"):
    if (tipoEscolhido == "metal"):
        print(relogioMetal)
    elif (tipoEscolhido == "couro"):
        print(relogioCouro)
    print("Ganhou Chaveiro")

# Quest 03

xeroxPB = 0.06
xeroxColor = 0.29
encard99 = 2.00
encard100 = 4.00
prec = 0

tipoServico = str.lower(input("Qual o tipo de serviço? "))
if (tipoServico == "encadernação"):
    quantFolhas = int(input("Quantas folhas?"))
    if (quantFolhas <= 100):
        preco = encard99
    else:
        preco = encard100
elif (tipoServico == "xérox"):
    quantPag = int(input("Quantas páginas? "))
    cor = str.lower(input("Colorida ou PB? "))
    if (cor == "pb"):
        preco = xeroxPB * quantPag
    else:
        preco = xeroxColor * quantPag
print("%.2f" % preco)

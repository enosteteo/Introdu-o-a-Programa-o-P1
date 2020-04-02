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
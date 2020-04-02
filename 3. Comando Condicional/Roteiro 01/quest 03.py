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
# Quest 01.b
pacote = 100
fotoPacote = 44.00
fotoAvulsa = 0.70

quantFotos = int(input("Quantas fotos desejas revelar? "))

totalPacote = quantFotos // pacote
totalAvulsa = quantFotos % pacote
totalPagarPacote = totalPacote * fotoPacote
totalPagarAvulsa = totalAvulsa * fotoAvulsa
totalAPagar = totalPagarPacote + totalPagarAvulsa

print("Serão necessários %i" % totalPacote, "pacote(s), e %i" %
      totalAvulsa, "avulsa(s), o valor total a ser pago é: R$ %.2f" % totalAPagar)
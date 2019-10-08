# Quest 01.a

rosa = 2.80
tulipa = 4.20

quantRosas = int(input("Quantas rosas desejas comprar? "))
quantTulipas = int(input("Quantas tulipas desejas comprar? "))

totalRosas = rosa * quantRosas
totalTulipas = tulipa * quantTulipas
totalNecessario = totalRosas + totalTulipas

print("O valor total necessário é: R$ %.2f" % totalNecessario)

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

# Quest 01.c

tempo = 60
quantHoras = int(input("Quantas horas? "))
quantMinutos = int(input("Quantos minutos? "))
quantSegundos = int(input("Quantos segundos? "))

quantHorasEmMinutos = quantHoras * tempo
quantMinutosTotal = quantHorasEmMinutos + quantMinutos
quantMinutosEmSegundos = quantMinutosTotal * tempo
quantSegundosTotal = quantMinutosEmSegundos + quantSegundos

print("Serão necessários %i" % quantSegundosTotal, "segundos.")

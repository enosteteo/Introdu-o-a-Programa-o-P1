# Quest 01.a

rosa = 2.80
tulipa = 4.20

quantRosas = int(input("Quantas rosas desejas comprar? "))
quantTulipas = int(input("Quantas tulipas desejas comprar? "))

totalRosas = rosa * quantRosas
totalTulipas = tulipa * quantTulipas
totalNecessario = totalRosas + totalTulipas

print("O valor total necessário é: R$ %.2f" % totalNecessario)
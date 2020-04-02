# Quest 04

promocao = 10

quantConvidados = int(input("Quantos foram convidados? "))
precoRodizio = float(input("Qual o valor do rodízio? "))

desconto = quantConvidados // promocao
quantPagantes = quantConvidados - desconto
totalAPagar = quantPagantes * precoRodizio

print("O valor total a ser pago é: %.2f" % totalAPagar)
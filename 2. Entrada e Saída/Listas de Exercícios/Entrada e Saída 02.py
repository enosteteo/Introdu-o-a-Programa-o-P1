# Quest 01

duziaLaranja = 12
precoDuziaLaranja = 9.00
precoUnidadeLaranja = precoDuziaLaranja / duziaLaranja

quantLaranja = int(input("Quantas laranjas desejas comprar? "))

precoLaranjas = quantLaranja * precoUnidadeLaranja

print("O valor a ser pago é: %.2f" % precoLaranjas)

# Quest 02

descontoIPVA = 5/100

ipva = float(input("Quanto é o IPVA? "))
taxa = float(input("Quanto é a taxa de trânsito? "))

descontoPagamentoIPAV = ipva * descontoIPVA
ipvaASerPago = ipva - descontoPagamentoIPAV
valorASerPago = ipvaASerPago + taxa

print("O total a ser pago é: %.2f" % valorASerPago)

# Quest 03

expedienteDiarioEmHoras = 8
horaTemMinutos = 60
expedienteDiarioEmMinutos = expedienteDiarioEmHoras * horaTemMinutos

quantMinPorProcesso = int(input("Quantos minutos por processo? "))

tempoNecessario = expedienteDiarioEmMinutos // quantMinPorProcesso

print("Betina pode analisar até:", tempoNecessario, "por dia")

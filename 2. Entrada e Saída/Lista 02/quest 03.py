# Quest 03

expedienteDiarioEmHoras = 8
horaTemMinutos = 60
expedienteDiarioEmMinutos = expedienteDiarioEmHoras * horaTemMinutos

quantMinPorProcesso = int(input("Quantos minutos por processo? "))

tempoNecessario = expedienteDiarioEmMinutos // quantMinPorProcesso

print("Betina pode analisar até:", tempoNecessario, "por dia")
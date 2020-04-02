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
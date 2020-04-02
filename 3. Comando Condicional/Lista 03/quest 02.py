# Quest 02
zero = 0
atrasoDuasHoras = 2
atrasoTresHoras = 3
ValorAtrasoDois = 30
ValorAtrasoTres = 80
ValorAtrasoMaiorTres = 40
valorAtraso = 0

diaria = float(input("Qual o valor da diária? "))
dias = int(input("Quantos dias? "))
atrasoEmHoras = int(input("Quantas horas de atraso? "))

valorDiarias = dias * diaria

if(atrasoEmHoras <= zero):
    valorAtraso = 0
elif (atrasoEmHoras < atrasoDuasHoras):
    valorAtraso = ValorAtrasoDois
elif (atrasoEmHoras <= atrasoTresHoras):
    valorAtraso = ValorAtrasoTres
elif (atrasoEmHoras > atrasoTresHoras):
    valorAtraso = atrasoEmHoras * ValorAtrasoMaiorTres

valorASerPago = diaria * dias + valorAtraso

print(valorASerPago)

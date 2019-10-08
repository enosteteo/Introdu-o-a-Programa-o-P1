# Quest 01

opcoes = [["gasolina", 2.53], ["etanol", 2.09], ["diesel", 1.92]]
promocaoDe = "etanol"
trocaOleo = 30

combustivel = str.lower(input("Qual o combustível a ser utilizado? "))
valorEmDinheiro = float(input("Quanto de %s? " % combustivel))
quantLitros = 0

if (combustivel == opcoes[0][0]):
    quantLitros = valorEmDinheiro / opcoes[0][1]

elif (combustivel == opcoes[1][0]):
    quantLitros = valorEmDinheiro / opcoes[1][1]

elif (combustivel == opcoes[2][0]):
    quantLitros = valorEmDinheiro / opcoes[2][1]

print("Litros -> %.2f" % quantLitros)
if ((quantLitros > trocaOleo) and (combustivel == promocaoDe)):
    print("Ganhou troca de Óleo")
else:
    print("Não ganhou troca de Óleo")

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

# Quest 03

tipoF = [["2d", 8.50], ["3d", 14.50]]
tipoC = [["combo simples", 10.00], ["combo completo", 12.00]]
tipoFilme = str.lower(input("Qual o tipo do filme? "))
tipoCombo = str.lower(input("Qual o tipo do lanche? "))
valorTotal = 0

if (tipoFilme == tipoF[0][0]):
    valorTotal += tipoF[0][1]

elif (tipoFilme == tipoF[1][0]):
    valorTotal += tipoF[1][1]

if (tipoCombo == tipoC[0][0]):
    valorTotal += tipoC[0][1]

elif (tipoCombo == tipoC[1][0]):
    valorTotal += tipoC[1][1]
print(valorTotal)

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
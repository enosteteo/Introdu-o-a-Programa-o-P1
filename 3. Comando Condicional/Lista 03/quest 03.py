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
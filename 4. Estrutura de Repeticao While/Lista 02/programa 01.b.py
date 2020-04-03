#Programa 01
# programa para ler 30 números
# exibir a quantidade de positivos

cont = 0
qtdePositivos = 0

while cont < 30:
    numero = int(input())
    if numero >= 0:
        qtdePositivos += 1
    cont += 1
print(qtdePositivos)
#Programa 01
# programa para ler 20 números
# exibir a soma dos pares

soma = 0
cont = 20
while cont > 0:
    numero = int(input())
    if (numero % 2) == 0:
        soma += numero
    cont -= 1
print(soma)

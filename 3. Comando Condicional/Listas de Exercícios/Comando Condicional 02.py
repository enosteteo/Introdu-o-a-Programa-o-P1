# Quest 01
num = int(input("Digite um número: "))
positivo = num > 0
negativo = num < 0
neutro = num == 0
if (positivo):
    print("Positivo")
elif(negativo):
    print("Negativo")
else:
    print("Neutro")

# Quest 02

num = int(input("Digite um número: "))
par = num % 2

if (par == 0):
    print("Par")
else:
    print("Ímpar")

# Quest 03

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

num1Ganha = num1 > num2
num2Ganha = num2 >= num3
num3Ganha = num3 >= num1

if(num1Ganha and num2Ganha):
    print("O maior número é %i" % num1)
elif(num2Ganha and num3Ganha):
    print("O maior número é %i" % num2)
else:
    print("O maior número é %i" % num3)

# Quest 04

zero = 0
par = 2
multiploDe = 3
divisorDe = 102

num = int(input("Digite um número: "))

numPar = num % par
numImpar = numPar > zero

multiplo = num % multiploDe
multiploTrue = multiplo > zero

divisor = divisorDe % num
divisorTrue = divisor > zero
if(numImpar):
    print("Número é ímpar")
else:
    print("Número não é ímpar")

if(multiploTrue):
    print("Número é múltiplo de %i" % multiploDe)
else:
    print("Número não é múltiplo de %i" % multiploDe)
if(divisorTrue):
    print("Número é divisor de %i" % divisorDe)
else:
    print("Número não é divisor de %i" % divisorDe)

# Quest 05

descontoDe = 10 / 100
aPartirDe = 100
descontoSePag = "dinheiro"
formasDePagamento = ["dinheiro", "cheque"]

valor = int(input("Valor da compra: "))
formaPag = str.lower(input("Forma de pagamento: "))

valorAPagar = valor
if(formaPag == formasDePagamento[0]):
    if(valor >= aPartirDe):
        desconto = valor * descontoDe
        valorAPagar = valor - desconto
    print("R$ %.2f" % valorAPagar)

elif (formaPag == formasDePagamento[1]):
    print("R$ %.2f" % valorAPagar)

else:
    print("Forma de Pagamento inválido")

# Quest 06

descontoDe = 10 / 100
aPartirDe = 100
quantParcelas = 3
descontoSePag = "dinheiro"
formasDePag = ["dinheiro", "cheque", "cartão"]
cartao = ["crédito", "débito"]

valor = int(input("Valor da compra: "))
formaPag = str.lower(input("Forma de pagamento: "))

valorAPagar = valor

if (formaPag == formasDePag[0]):
    if(valor >= aPartirDe):
        desconto = valor * descontoDe
        valorAPagar = valor - descontoDe
    print("R$ %.2f" % valorAPagar)

elif (formaPag == formasDePag[1]):
    print("R$ %.2f" % valorAPagar)

elif (formaPag == formasDePag[2]):
    func = str.lower(input("Qual a função? "))
    if(func == cartao[0]):
        parcela = int(input("Quantas parcelas? "))
        if(parcela <= quantParcelas):
            valorAPagar = valor / parcela
            print("R$ %.2f" % valor)
            print("%i" % parcela, "parcelas de R$ %.2f" % valorAPagar)
        else:
            print("Quantidade de parcelas inválidas.")
    elif(func == cartao[1]):
        print("R$ %.2f" % valorAPagar)
    else:
        print("função inválida")
else:
    print("Forma de Pagamento inválido")

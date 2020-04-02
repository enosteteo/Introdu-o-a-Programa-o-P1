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

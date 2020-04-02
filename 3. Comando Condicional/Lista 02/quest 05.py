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
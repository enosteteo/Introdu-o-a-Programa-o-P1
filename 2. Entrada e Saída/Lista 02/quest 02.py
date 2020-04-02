
# Quest 02

descontoIPVA = 5/100

ipva = float(input("Quanto é o IPVA? "))
taxa = float(input("Quanto é a taxa de trânsito? "))

descontoPagamentoIPAV = ipva * descontoIPVA
ipvaASerPago = ipva - descontoPagamentoIPAV
valorASerPago = ipvaASerPago + taxa

print("O total a ser pago é: %.2f" % valorASerPago)
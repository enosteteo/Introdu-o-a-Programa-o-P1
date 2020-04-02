# Quest 01

valorHoraAcesso = 2.30
horaTemMinutos = 60
valorMinutoAcesso = valorHoraAcesso / horaTemMinutos

minutosDeUso = int(input("Quantos minutos o cliente passou utilizando? "))

valorASerPago = minutosDeUso * valorMinutoAcesso

print("O valor a ser pago é: %.2f" % valorASerPago)
# Quest 05

precoQuilo = 20.00
pratoVazio = 230
kilograma = 1000

pratoCliente = int(input("Quantos gramas deu o almoço do cliente? "))

pesoTotalGrama = pratoCliente - pratoVazio
pesoKg = pesoTotalGrama / kilograma
precoCobrado = pesoKg * precoQuilo

print("O valor a ser pago é: %.2f" % precoCobrado)
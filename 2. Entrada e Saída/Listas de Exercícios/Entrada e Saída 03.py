# Quest 01

valorHoraAcesso = 2.30
horaTemMinutos = 60
valorMinutoAcesso = valorHoraAcesso / horaTemMinutos

minutosDeUso = int(input("Quantos minutos o cliente passou utilizando? "))

valorASerPago = minutosDeUso * valorMinutoAcesso

print("O valor a ser pago é: %.2f" % valorASerPago)

# Quest 02

kilograma = 1000
consumoCarne = 500 / kilograma
consumoCerveja = 6
precoKiloCarne = 17.00
precoUndCerveja = 1.80

consumoCarnePessoa = consumoCarne * precoKiloCarne
consumoCervejaPessoa = consumoCerveja * precoUndCerveja

quantPessoas = int(input("Quantas pessoas serão convidadas? "))

consumoCarneTotal = quantPessoas * consumoCarnePessoa
consumoCervejaTotal = quantPessoas * consumoCervejaPessoa
print("Será gasto um total de R$ %.2f " % consumoCarneTotal,
      "em carne, e R$ %.2f " % consumoCervejaTotal, "em cerveja")

# Quest 03

totalRevistas = int(input("Quantidade total de revistas: "))
quantAmigos = int(input("Quantos amigos serão beneficiados? "))

quantDoadas = totalRevistas // quantAmigos
quantResta = totalRevistas % quantAmigos

print("Cada amigo de Sheldon irá receber %i" %
      quantDoadas, "e irá restar: %i" % quantResta)

# Quest 04

promocao = 10

quantConvidados = int(input("Quantos foram convidados? "))
precoRodizio = float(input("Qual o valor do rodízio? "))

desconto = quantConvidados // promocao
quantPagantes = quantConvidados - desconto
totalAPagar = quantPagantes * precoRodizio

print("O valor total a ser pago é: %.2f" % totalAPagar)

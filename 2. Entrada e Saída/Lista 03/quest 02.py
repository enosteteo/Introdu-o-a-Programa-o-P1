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
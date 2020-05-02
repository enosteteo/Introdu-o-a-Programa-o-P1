tipo = ["crédito", "débito"]
qtdeCredito = 0
saldo = 0
ent_tipo = input("Tipo: ").lower()
while ent_tipo in tipo:
    ent_val = float(input("Valor: "))
    if ent_tipo == tipo[0]:
        saldo += ent_val
        qtdeCredito += 1
    elif ent_tipo == tipo[1]:
        saldo -= ent_val
    ent_tipo = input("Tipo: ").lower()

print("Quantidade de créditos: %i" % qtdeCredito)
if saldo >= 0:
    print("Saldo financeiro: R$ %.2f" % saldo)
    print("Saldo Positivo")
if saldo < 0:
    print("Saldo financeiro: - R$ %.2f" % (saldo * -1))
    print("Saldo Negativo")
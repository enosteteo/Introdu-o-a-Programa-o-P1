maxi_convidados = 15
maxi_excetende = 10
maxi_permitido = maxi_convidados + maxi_excetende
val_unit_excedente = 42
qtdeConvidados = 0
total = 0
execute = "sim"
while execute == "sim":
    conv = int(input("Qtde Convidados: "))
    if conv > maxi_convidados:
        if conv > maxi_permitido:
            conv = maxi_permitido
        total += val_unit_excedente * (conv - maxi_convidados)
    qtdeConvidados += conv + 1
    execute = input("Repetir?").lower()
print("%.2f " % total)
print(qtdeConvidados)
# Quest 02

itens = [["bolsa", ["couro", 180], ["tecido", 100]],
         ["relógio", ["metal", 215], ["couro", 150]]]

bolsaCouro = 180
bolsaTecido = 100
relogioMetal = 215
relogioCouro = 150
brinde = "relógio"
preco = 0

presenteEscolhido = str.lower(input("Qual o presente escolhido? "))
tipoEscolhido = str.lower(input("Qual o tipo escolhido? "))

if (presenteEscolhido == "bolsa"):
    if (tipoEscolhido == "couro"):
        print(bolsaCouro)
    elif (tipoEscolhido == "tecido"):
        print(bolsaTecido)
elif (presenteEscolhido == "relógio"):
    if (tipoEscolhido == "metal"):
        print(relogioMetal)
    elif (tipoEscolhido == "couro"):
        print(relogioCouro)
    print("Ganhou Chaveiro")
# Quest 04

garantiaUm = 3 / 100
garantiaDois = 5 / 100

valorProduto = float(input("Qual o valor do produto? "))
tempoGarantia = int(input("Garantia de quanto tempo? "))

if (tempoGarantia == 1):
    preco = valorProduto * garantiaUm
    valorProduto = valorProduto + preco
elif (tempoGarantia == 2):
    preco = valorProduto * garantiaDois
    valorProduto = valorProduto + preco
print("%.2f" % valorProduto)
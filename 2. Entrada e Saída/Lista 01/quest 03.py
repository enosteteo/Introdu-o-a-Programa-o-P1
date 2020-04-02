# Quest 03

copia = 0.08
paginaPorFolha = 2

quantFolhas = int(input("O livro possui quantas folhas? "))

quantPaginas = quantFolhas * paginaPorFolha
valorTotal = copia * quantPaginas

print("O total a ser pago é: %.2f" % valorTotal)
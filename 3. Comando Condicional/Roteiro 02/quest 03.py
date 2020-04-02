# Quest 03

conceitoA = 1 / 8
conceitoB = 1 / 12
conceitoC = 1 / 18
conceitoD = 1 / 18

quantLivros = int(input("Quantidade de livros: "))
quantAlunos = int(input("Quantidade de alunos: "))
conceito = quantLivros / quantAlunos

if conceito < conceitoD:
    print("D")
elif conceito <= conceitoC:
    print("C")
elif conceito <= conceitoB:
    print("B")
else:
    print("A")
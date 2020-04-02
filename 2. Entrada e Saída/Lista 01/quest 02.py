# Quest 02

horaAula = 35.00
projeto = 80.00

horaMes = int(
    input("Quantas horas o professor esteve na sala de aula durante o mês? "))
quantProjetosOrientados = int(input("Quantos projetos o professor orientou? "))

salarioAula = horaAula * horaMes
salarioProjeto = projeto * quantProjetosOrientados
salarioTotal = salarioAula + salarioProjeto

print("O salario a ser recebido pelo professor é: %.2f" % salarioTotal)

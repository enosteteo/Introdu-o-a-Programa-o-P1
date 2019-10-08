'  # Quest 01
# sequencia = [int, String, int, float, String,
#            String, float, int, float, String]

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

# Quest 03

copia = 0.08
paginaPorFolha = 2

quantFolhas = int(input("O livro possui quantas folhas? "))

quantPaginas = quantFolhas * paginaPorFolha
valorTotal = copia * quantPaginas

print("O total a ser pago é: %.2f" % valorTotal)

# Quest 04

multa = 0.75

diasAtraso = int(input("O quantos dias de atraso? "))

multaASerPaga = multa * diasAtraso

print("O valor da multa a ser paga é: %.2f" % multaASerPaga)

# Quest 05

precoQuilo = 20.00
pratoVazio = 230
kilograma = 1000

pratoCliente = int(input("Quantos gramas deu o almoço do cliente? "))

pesoTotalGrama = pratoCliente - pratoVazio
pesoKg = pesoTotalGrama / kilograma
precoCobrado = pesoKg * precoQuilo

print("O valor a ser pago é: %.2f" % precoCobrado)

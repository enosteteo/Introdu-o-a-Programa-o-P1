portugues = 50
matematica = 35
redacao = 1

requisitoPortugues = 0.8 * portugues
requisitoMatematica = 0.6 * matematica
requisitoRedacao = 7

qtdeAprovados = 0

notaPortugues = int(input("Qtde Questões acertadas - Português: "))
while notaPortugues > 0:
    notaMatematica = int(input("Qtde Questões acertadas - Matetática: "))
    notaRedacao = float(input("Nota - Redação: "))
    aprovadoPortugues = notaPortugues >= requisitoPortugues
    aprovadoMatematica = notaMatematica >= requisitoMatematica
    aprovadoRedacao = notaRedacao >= requisitoRedacao
    if aprovadoRedacao and aprovadoPortugues and aprovadoMatematica:
        qtdeAprovados += 1
    notaPortugues = int(input("Qtde Questões acertadas - Português: "))
print("%i" % qtdeAprovados)
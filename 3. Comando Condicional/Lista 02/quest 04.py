# Quest 04

zero = 0
par = 2
multiploDe = 3
divisorDe = 102

num = int(input("Digite um número: "))

numPar = num % par
numImpar = numPar > zero

multiplo = num % multiploDe
multiploTrue = multiplo > zero

divisor = divisorDe % num
divisorTrue = divisor > zero
if(numImpar):
    print("Número é ímpar")
else:
    print("Número não é ímpar")

if(multiploTrue):
    print("Número é múltiplo de %i" % multiploDe)
else:
    print("Número não é múltiplo de %i" % multiploDe)
if(divisorTrue):
    print("Número é divisor de %i" % divisorDe)
else:
    print("Número não é divisor de %i" % divisorDe)
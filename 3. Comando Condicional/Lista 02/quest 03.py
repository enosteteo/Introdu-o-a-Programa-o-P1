# Quest 03

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

num1Ganha = num1 > num2
num2Ganha = num2 >= num3
num3Ganha = num3 >= num1

if(num1Ganha and num2Ganha):
    print("O maior número é %i" % num1)
elif(num2Ganha and num3Ganha):
    print("O maior número é %i" % num2)
else:
    print("O maior número é %i" % num3)
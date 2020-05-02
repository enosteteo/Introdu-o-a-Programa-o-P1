jovem = 19
adulto = 60
idoso = 61

qtdeJovem = 0
qtdeIdoso = 0
maiorIdadeAdulto = 0
somaIdadeIdoso = 0


idade = int(input("idade: "))
while idade >= 0:
    if idade <= jovem:
        qtdeJovem += 1
    elif maiorIdadeAdulto < idade <= adulto:
        maiorIdadeAdulto = idade
    elif idade >= idoso:
        somaIdadeIdoso += idade
        qtdeIdoso += 1
    idade = int(input("idade: "))

if qtdeJovem != 0:
    print("Quantidade de Jovens -> %i" % qtdeJovem)
else:
    print("Não há jovens")

if maiorIdadeAdulto != 0:
    print("Maior idade Adulto -> %i" % maiorIdadeAdulto)
else:
    print("Não há adultos")

if qtdeIdoso != 0:
    mediaIdadeIdoso = somaIdadeIdoso / qtdeIdoso
    print("Média idade idoso -> %i" % mediaIdadeIdoso)
else:
    print("Não há idosos")
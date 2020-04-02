# Quest 03

totalRevistas = int(input("Quantidade total de revistas: "))
quantAmigos = int(input("Quantos amigos serão beneficiados? "))

quantDoadas = totalRevistas // quantAmigos
quantResta = totalRevistas % quantAmigos

print("Cada amigo de Sheldon irá receber %i" %
      quantDoadas, "e irá restar: %i" % quantResta)
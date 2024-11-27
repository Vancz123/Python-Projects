input = str(input("Voce e Macho ou Femea? responder com F ou M  "))
genero = input.upper()

if genero == "M":
    print("Masculino")

elif genero == 'F':
    print("Feminino")

else:
    print("Genero Invalido")
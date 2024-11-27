def Compara():
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))

    if n1 > n2:
        print(f"O primeiro número ({n1}) é maior que o segundo ({n2}).")
    elif n1 < n2:
        print(f"O segundo número ({n2}) é maior que o primeiro ({n1}).")
    else:
        print("Os dois números são iguais.")



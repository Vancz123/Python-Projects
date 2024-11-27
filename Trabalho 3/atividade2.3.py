import random

n_aleatorio = random.randint(0, 10)

tentativas = []

print("Pensa num número entre 0 e 10")

while True:
    numeroaleatorio = int(input("Digita um numero aleatorio: "))

    tentativas.append(numeroaleatorio)

    if numeroaleatorio == n_aleatorio:
        print("Acertou!!")
        break
    else:
        print("Tente novamente!")

print(f"Você acertou em {len(tentativas)} tentativas.")

def calcular_notas(valor):
    notas = [200, 100, 50, 20, 10, 5]
    resultado = {}

    for nota in notas:
        if valor >= nota:
            quantidade = valor // nota
            valor = valor % nota
            resultado[nota] = quantidade

    return resultado


def main():
    print("Bem-vindo à Caixa de Multibanco")

    while True:
        try:
            valor = int(input("Qual o valor que pretende levantar? "))

            if valor < 10 or valor > 400:
                print("O valor deve estar entre 10€ e 400€. Por favor, tente novamente.")
            elif valor % 5 != 0:
                print("O valor deve ser múltiplo de 5. Por favor, tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor válido.")

    notas_necessarias = calcular_notas(valor)

    print(f"Para levantar {valor}€, irá receber:")
    for nota, quantidade in notas_necessarias.items():
        print(f"{quantidade} nota(s) de {nota}€")


if __name__ == "__main__":
    main()

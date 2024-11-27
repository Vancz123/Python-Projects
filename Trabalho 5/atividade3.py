def obter_inteiro():
    while True:
        try:
            valor = float(input("Insira um número inteiro: "))
            if valor.is_integer():
                return int(valor)  # Converte para inteiro se for válido
            else:
                print("Erro: O valor inserido não é um número inteiro.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.")


def obter_real():
    while True:
        try:
            valor = float(input("Insira um número real (float): "))
            return valor  # Retorna o valor float válido
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número real.")


# Função principal
def float_valido():
    inteiro_valido = obter_inteiro()
    real_valido = obter_real()

    print(f"Valor inteiro inserido: {inteiro_valido}")
    print(f"Valor real inserido: {real_valido}")


float_valido()

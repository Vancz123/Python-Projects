def calcular_salario(salario_base, horas_extra, valor_hora, descontos):
    try:
        salario = salario_base + (horas_extra * valor_hora) - (descontos * 100) / 100
        return salario
    except Exception as e:
        print(f"Ocorreu um erro durante o cálculo: {e}")
        return None


def obter_valores():
    try:
        salario_base = float(input("Digite o salário base do funcionário: "))
        horas_extra = float(input("Digite o número de horas extras: "))
        valor_hora = float(input("Digite o valor pago por hora extra: "))
        descontos = float(input("Digite o valor dos descontos: "))

        salario = calcular_salario(salario_base, horas_extra, valor_hora, descontos)

        if salario is not None:
            print(f"O salário final do funcionário é:  {salario:.2f} €")
    except ValueError:
        print("Entrada inválida! Por favor, insira valores numéricos corretos.")


(obter_valores())

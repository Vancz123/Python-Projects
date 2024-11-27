
def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

def inserir_dados_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")


    freq_respiratoria = obter_float("Digite a frequência respiratória do paciente (em respirações por minuto): ")
    temperatura = obter_float("Digite a temperatura do paciente (em °C): ")
    freq_cardiaca = obter_float("Digite a frequência cardíaca do paciente (em batimentos por minuto): ")

    dados_paciente = {
        "Nome": nome,
        "Idade": idade,
        "Frequência Respiratória": freq_respiratoria,
        "Temperatura": temperatura,
        "Frequência Cardíaca": freq_cardiaca
    }

    nome_arquivo = f"{nome.lower().replace(' ', '_')}.txt"

    with open(nome_arquivo, "w") as arquivo:
        for chave, valor in dados_paciente.items():
            arquivo.write(f"{chave}: {valor}\n")

    print(f"Dados do paciente {nome} gravados com sucesso no ficheiro '{nome_arquivo}'\n")


def mypatient():
    while True:
        inserir_dados_paciente()
        continuar = input("Deseja inserir os dados de outro paciente? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando o programa.")
            break

mypatient()


def carregar_dados_paciente(nome_arquivo):
    dados_paciente = {}
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split(": ")
                dados_paciente[chave] = valor
        return dados_paciente
    except FileNotFoundError:
        print(f"Ficheiro '{nome_arquivo}' não encontrado.")
        return None

def avaliar_saude(dados_paciente):
    try:
        freq_respiratoria = float(dados_paciente["Frequência Respiratória"])
        temperatura = float(dados_paciente["Temperatura"])
        freq_cardiaca = float(dados_paciente["Frequência Cardíaca"])
    except KeyError as e:
        return f"Erro: dado ausente no arquivo ({str(e)})."
    except ValueError:
        return "Erro: valor inválido nos dados do paciente."

    doente = False
    diagnostico = []

    if not (12 <= freq_respiratoria <= 20):
        diagnostico.append("Frequência respiratória fora do normal.")
        doente = True

    if not (36 <= temperatura <= 37.5):
        diagnostico.append("Temperatura fora do normal.")
        doente = True

    if not (60 <= freq_cardiaca <= 100):
        diagnostico.append("Frequência cardíaca fora do normal.")
        doente = True

    if doente:
        return f"Paciente está doente. Problemas detectados: {'; '.join(diagnostico)}"
    else:
        return "Paciente está saudável."

def diagnostico():
    while True:
        nome_arquivo = input("Digite o nome do ficheiro do paciente para avaliar (ou 'sair' para encerrar): ")

        if nome_arquivo.lower() == "sair":
            print("Encerrando o programa.")
            break

        if not nome_arquivo.endswith(".txt"):
            nome_arquivo += ".txt"

        dados_paciente = carregar_dados_paciente(nome_arquivo)

        if dados_paciente:
            resultado = avaliar_saude(dados_paciente)
            print(resultado)

        continuar = input("Deseja avaliar outro paciente? (sim/não): ").strip().lower()
        if continuar != "s":
            print("Encerrando o programa.")
            break

diagnostico()

import os

def analisar_ficheiro(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            linhas = ficheiro.readlines()

        num_linhas = len(linhas)
        num_linhas_vazias = sum(1 for linha in linhas if linha.strip() == '')
        num_frases = sum(linha.count('.') + linha.count('!') + linha.count('?') for linha in linhas)
        num_palavras = sum(len(linha.split()) for linha in linhas)

        print(f"Resultados para o ficheiro '{nome_ficheiro}':")
        print(f"Número total de linhas: {num_linhas}")
        print(f"Número de linhas vazias: {num_linhas_vazias}")
        print(f"Número de frases: {num_frases}")
        print(f"Número de palavras: {num_palavras}")

    except FileNotFoundError:
        print(
            f"Não foi possível abrir o ficheiro '{nome_ficheiro}'. Verifique se o nome está correto e tente novamente.")


nome_ficheiro = input("Digite o nome do ficheiro (com extensão): ")
analisar_ficheiro(nome_ficheiro)
#utilize o ficheiro que criei atividade1.txt para este exercicio tambem
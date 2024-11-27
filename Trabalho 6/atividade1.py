def pesquisar_palavra_no_ficheiro(nome_ficheiro, palavra):
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            linhas = ficheiro.readlines()

        palavra_normalizada = palavra.lower()

        linhas_encontradas = []

        for numero_linha, linha in enumerate(linhas, start=1):
            if palavra_normalizada in linha.lower():
                linhas_encontradas.append((numero_linha, linha.strip()))

        if linhas_encontradas:
            print(f"A palavra '{palavra}' foi encontrada nas seguintes linhas:")
            for numero_linha, conteudo in linhas_encontradas:
                print(f"Linha {numero_linha}: {conteudo}")
        else:
            print(f"A palavra '{palavra}' não foi encontrada no ficheiro.")

    except FileNotFoundError:
        print(f"O ficheiro '{nome_ficheiro}' não foi encontrado.")


nome_ficheiro = input("Digite o nome do ficheiro (com extensão): ")
palavra = input("Digite a palavra a ser pesquisada: ")
pesquisar_palavra_no_ficheiro(nome_ficheiro, palavra)

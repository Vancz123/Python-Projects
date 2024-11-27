def criar_dicionario_produtos():
    # Dicionário de produtos com nome e preço
    produtos = {
        'Arroz': 1.5,
        'Feijão': 2.0,
        'Açúcar': 1.2,
        'Leite': 0.9,
        'Pão': 0.5,
        'Ovos': 2.5,
        'Manteiga': 1.8,
        'Queijo': 3.0,
        'Café': 4.5,
        'Frango': 5.0
    }
    return produtos


def exibir_produtos(produtos):
    print("Produtos disponíveis:")
    for produto, preco in produtos.items():
        print(f"{produto}: €{preco:.2f}")


def fazer_compras(produtos):
    compras = {}
    while True:
        produto = input("Digite o nome do produto que deseja comprar (ou 'sair' para terminar): ").capitalize()
        if produto == 'Sair':
            break
        elif produto not in produtos:
            print("Produto não encontrado. Tente novamente.")
            continue

        quantidade = int(input(f"Digite a quantidade de {produto} que deseja comprar: "))

        if produto in compras:
            compras[produto] += quantidade
        else:
            compras[produto] = quantidade

    return compras


def calcular_total(compras, produtos):
    total = 0
    for produto, quantidade in compras.items():
        total += produtos[produto] * quantidade
    return total


def exibir_talao(compras, produtos, total):
    print("\n--- Talão de Compras ---")
    for produto, quantidade in compras.items():
        preco_total_produto = produtos[produto] * quantidade
        print(f"{produto}: {quantidade} x €{produtos[produto]:.2f} = €{preco_total_produto:.2f}")
    print(f"\nTotal a pagar: €{total:.2f}")


def gravar_talao_em_ficheiro(compras, produtos, total, nome_ficheiro="talaoCompra.txt"):
    with open(nome_ficheiro, 'w', encoding='utf-8') as ficheiro:
        ficheiro.write("--- Talão de Compras ---\n")
        for produto, quantidade in compras.items():
            preco_total_produto = produtos[produto] * quantidade
            ficheiro.write(f"{produto}: {quantidade} x €{produtos[produto]:.2f} = €{preco_total_produto:.2f}\n")
        ficheiro.write(f"\nTotal a pagar: €{total:.2f}\n")
    print(f"\nTalão de compras guardado em '{nome_ficheiro}'.")


# Função principal
def total():
    produtos = criar_dicionario_produtos()
    exibir_produtos(produtos)
    compras = fazer_compras(produtos)

    if compras:
        total = calcular_total(compras, produtos)
        exibir_talao(compras, produtos, total)
        gravar_talao_em_ficheiro(compras, produtos, total)
    else:
        print("Nenhum produto foi comprado.")

total()

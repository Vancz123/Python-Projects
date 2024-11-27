def lista_organizada(lista, valor):
    if not lista:
        lista.append(valor)
    else:
        i = 0
        while i < len(lista) and lista[i] < valor:
            i += 1
        lista.insert(i, valor)


def lista():
    n = int(input("Quantos elementos terá a lista? "))

    lista = []

    for _ in range(n):
        valor = int(input("Insira um valor inteiro: "))
        lista_organizada(lista, valor)  # Insere o valor de forma ordenada

    print("Lista ordenada:", lista)

lista()

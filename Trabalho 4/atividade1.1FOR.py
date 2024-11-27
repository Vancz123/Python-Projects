def lista_for(lista):
    if not lista:
        return 0

    max_valor = lista[0]
    i = 1

    while i < len(lista):
        if lista[i] > max_valor:
            max_valor = lista[i]
        i += 1

    return max_valor

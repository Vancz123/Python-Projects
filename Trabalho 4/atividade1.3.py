def encontrar_numeros_unicos(lista):
    unicos = []
    unicos.sort

    for num in lista:
        if lista.count(num) == 1:
            unicos.append(num)

    if unicos:
        print("Números que aparecem apenas uma vez:", unicos)
    else:
        print("Não há nenhum número que apareça apenas uma vez na lista.")


lista = [4, 5, 6, 7, 5, 6, 8, 9, 9, 10, 12, 13]
encontrar_numeros_unicos(lista)

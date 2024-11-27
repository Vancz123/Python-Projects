# Lista para armazenar os formandos
formandos = []


# Função para adicionar formandos
def adicionar_formando(nome, genero, idade, localidade, curso):
    formando = {
        'Nome': nome,
        'Género': genero,
        'Idade': idade,
        'Localidade': localidade,
        'Curso': curso
    }
    formandos.append(formando)


# Função para calcular o número de formandos e quantos estão inscritos no curso de Python
def informaçao():
    total_formandos = len(formandos)
    formandos_python = sum(1 for formando in formandos if formando['Curso'] == 'Python')

    print(f"A. Número de formandos registados: {total_formandos}")
    print(f"B. Número de formandos inscritos no curso de Python: {formandos_python}")

#adiçao de formandos a lista
adicionar_formando("Maria", "Feminino", 25, "Leiria", "Python")
adicionar_formando("João", "Masculino", 30, "Porto", "Java")
adicionar_formando("Pedro", "Masculino", 22, "Lisboa", "Python")

# Exibir estatísticas
informaçao()

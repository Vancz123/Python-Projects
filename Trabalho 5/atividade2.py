# Lista para armazenar os alunos da turma
turma = []


# Função para adicionar alunos à turma
def adicionar_aluno(nome, genero, nota_final):
    aluno = {
        'Nome': nome,
        'Género': genero,
        'Nota Final': nota_final
    }
    turma.append(aluno)


# Função para calcular a média de notas da turma
def calcular_media_notas():
    total_notas = sum(aluno['Nota Final'] for aluno in turma)
    return total_notas / len(turma) if turma else 0


# Função para exibir estatísticas da turma
def estatisticas():
    total_alunos = len(turma)
    media_notas = calcular_media_notas()

    # Alunos masculinos e femininos
    alunos_masculinos = [aluno['Nome'] for aluno in turma if aluno['Género'].lower() == 'masculino']
    alunos_femininos = [aluno['Nome'] for aluno in turma if aluno['Género'].lower() == 'feminino']

    # Alunos com notas acima e abaixo da média
    alunos_acima_media = [aluno['Nome'] for aluno in turma if aluno['Nota Final'] > media_notas]
    alunos_abaixo_media = [aluno['Nome'] for aluno in turma if aluno['Nota Final'] < media_notas]

    print(f"1. Número de alunos na turma: {total_alunos}")
    print(f"2. Média das notas da turma: {media_notas:.2f}")
    print(f"3. Alunos masculinos: {', '.join(alunos_masculinos) if alunos_masculinos else 'Nenhum'}")
    print(f"4. Alunos femininos: {', '.join(alunos_femininos) if alunos_femininos else 'Nenhum'}")
    print(f"5. Alunos com nota acima da média: {', '.join(alunos_acima_media) if alunos_acima_media else 'Nenhum'}")
    print(f"6. Alunos com nota abaixo da média: {', '.join(alunos_abaixo_media) if alunos_abaixo_media else 'Nenhum'}")


adicionar_aluno("Ana", "Feminino", 16)
adicionar_aluno("João", "Masculino", 14)
adicionar_aluno("Pedro", "Masculino", 18)
adicionar_aluno("Maria", "Feminino", 12)

estatisticas()

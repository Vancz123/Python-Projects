from alunos import Aluno
from disciplinas import Disciplina

turma = []


def registrar_aluno():
    nome = input("Nome do aluno: ")
    aluno = Aluno(nome)
    turma.append(aluno)
    print(f"Aluno {nome} registrado com sucesso.")


def registrar_disciplina():
    nome_aluno = input("Nome do aluno: ")
    aluno = next((al for al in turma if al.nome == nome_aluno), None)
    if aluno:
        nome_disciplina = input("Nome da disciplina: ")
        disciplina = Disciplina(nome_disciplina)
        aluno.adicionar_disciplina(disciplina)
        print(f"Disciplina {nome_disciplina} adicionada para {nome_aluno}.")
    else:
        print(f"Aluno {nome_aluno} não encontrado.")


def registrar_modulo():
    nome_aluno = input("Nome do aluno: ")
    nome_disciplina = input("Nome da disciplina: ")
    nome_modulo = input("Nome do módulo: ")

    aluno = next((al for al in turma if al.nome == nome_aluno), None)
    if aluno and nome_disciplina in aluno.disciplinas:
        aluno.disciplinas[nome_disciplina].adicionar_modulo(nome_modulo)
        print(f"Módulo {nome_modulo} registado em {nome_disciplina} para {nome_aluno}.")
    else:
        print(f"Aluno ou disciplina não encontrado.")


def registrar_nota():
    nome_aluno = input("Nome do aluno: ")
    nome_disciplina = input("Nome da disciplina: ")
    nome_modulo = input("Nome do módulo: ")
    nota = float(input("Nota do módulo: "))

    aluno = next((al for al in turma if al.nome == nome_aluno), None)
    if aluno and nome_disciplina in aluno.disciplinas:
        aluno.disciplinas[nome_disciplina].registrar_nota_modulo(nome_modulo, nota)
        print(f"Nota {nota} registrada para módulo {nome_modulo} em {nome_disciplina}.")
    else:
        print(f"Aluno ou disciplina não encontrado.")


def calcular_media():
    nome_aluno = input("Nome do aluno: ")
    nome_disciplina = input("Nome da disciplina: ")

    aluno = next((al for al in turma if al.nome == nome_aluno), None)
    if aluno and nome_disciplina in aluno.disciplinas:
        media = aluno.disciplinas[nome_disciplina].calcular_media()
        print(f"Média da disciplina {nome_disciplina} para {nome_aluno}: {media}")
    else:
        print(f"Aluno ou disciplina não encontrado.")


def gravar_dados():
    with open("registo_turma.txt", "w") as file:
        for aluno in turma:
            file.write(f"{aluno}\n")
            for nome_disciplina, disciplina in aluno.disciplinas.items():
                file.write(f"  {disciplina}\n")
                for nome_modulo, nota in disciplina.modulos.items():
                    file.write(f"    Módulo: {nome_modulo} - Nota: {nota}\n")
    print("Dados salvos em registo_turma.txt.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Registar aluno")
        print("2. Registar disciplina")
        print("3. Registar módulo")
        print("4. Registar nota")
        print("5. Calcular média")
        print("6. Gravar dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_aluno()
        elif opcao == "2":
            registrar_disciplina()
        elif opcao == "3":
            registrar_modulo()
        elif opcao == "4":
            registrar_nota()
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            gravar_dados()
        elif opcao == "0":
            print("A Fechar o Programa!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = {}

    def adicionar_disciplina(self, disciplina):
        self.disciplinas[disciplina.nome] = disciplina

    def __str__(self):
        return f"Aluno: {self.nome}"

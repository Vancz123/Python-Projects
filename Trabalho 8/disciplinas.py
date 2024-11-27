class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.modulos = {}

    def adicionar_modulo(self, nome_modulo, nota=0):
        self.modulos[nome_modulo] = nota

    def registrar_nota_modulo(self, nome_modulo, nota):
        if nome_modulo in self.modulos:
            self.modulos[nome_modulo] = nota
        else:
            print(f"Módulo {nome_modulo} não encontrado.")

    def calcular_media(self):
        if len(self.modulos) == 0:
            return 0
        return sum(self.modulos.values()) / len(self.modulos)

    def __str__(self):
        return f"Disciplina: {self.nome}"

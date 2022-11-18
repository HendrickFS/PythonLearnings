class Aluno:
    def __init__(self, nome=None, ra=None, endereco=None, idade=None, nome_curso=None):
        self.nome = nome
        self.ra = ra
        self.endereco = endereco
        self.idade = idade
        self.nome_curso = nome_curso

    def __str__(self):
        return f'Nome: {self.nome} RA: {self.ra} Endereço: {self.endereco} Idade: {self.idade} Nome do curso: {self.nome_curso}'
    
    def __eq__(self, outro):
        return self.ra == outro.ra
    
    def aumentaIdade(self):
        self.idade += 1

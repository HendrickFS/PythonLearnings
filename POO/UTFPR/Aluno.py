class Aluno:
    def __init__(self, ra, nome, nomeMeio, sobrenome, identidade, nacionalidade, dataNascimento, curso, turno):
        self.ra = ra
        self.nome = nome
        self.nomeMeio = nomeMeio
        self.sobrenome = sobrenome
        self.identidade = identidade
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento
        self.dataIngresso = ''
        self.situação = "Regular"
        self.coeficiente = 0
        self.curso = curso
        self.turno = turno
        self.disciplinas = []
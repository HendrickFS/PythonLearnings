class Professor:
    def __init__(self, matricula, nome, nomeMeio, sobrenome, identidade, nacionalidade, dataNascimento, departamento):
        self.matricula = matricula
        self.nome = nome
        self.nomeMeio = nomeMeio
        self.sobrenome = sobrenome
        self.identidade = identidade
        self.nacionalidade = nacionalidade
        self.dataNascimento = dataNascimento
        self.dataAdmissao = ''
        self.departamento = departamento
        self.disciplinas = []
class Disciplina:
    def __init__(self, codigo, nome, ano, semestre, professor, modalidade, cargaHoraria, objetivo, ementa, bibliografia):
        self.codigo = codigo
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.professor = professor
        self.alunos = []
        self.modalidade = modalidade
        self.cargaHoraria = cargaHoraria
        self.objetivo = objetivo
        self.ementa = ementa
        self.bibliografia = bibliografia
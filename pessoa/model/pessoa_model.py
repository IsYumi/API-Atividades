from database.database import db


class Professor(db.Model):
    __tablename__ = 'professores'

    id_professor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id_professor': self.id_professor,
            'nome': self.nome
        }



class Aluno(db.Model):
    __tablename__ = 'alunos'

    id_aluno = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id_aluno': self.id_aluno,
            'nome': self.nome
        }


alunos_disciplinas = db.Table('alunos_disciplinas',
    db.Column('id_aluno', db.Integer, db.ForeignKey('alunos.id_aluno'), primary_key=True),
    db.Column('id_disciplina', db.Integer, db.ForeignKey('disciplinas.id_disciplina'), primary_key=True)
)

professores_disciplinas = db.Table('professores_disciplinas',
    db.Column('id_professor', db.Integer, db.ForeignKey('professores.id_professor'), primary_key=True),
    db.Column('id_disciplina', db.Integer, db.ForeignKey('disciplinas.id_disciplina'), primary_key=True)
)



class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id_disciplina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    publica = db.Column(db.Boolean, default=False)

    alunos = db.relationship('Aluno', secondary=alunos_disciplinas, backref='disciplinas')
    professores = db.relationship('Professor', secondary=professores_disciplinas, backref='disciplinas')

    def to_dict(self):
        return {
            'id_disciplina': self.id_disciplina,
            'nome': self.nome,
            'publica': self.publica,
            'alunos': [aluno.id_aluno for aluno in self.alunos],
            'professores': [prof.id_professor for prof in self.professores]
        }

professores = [
    {'nome': "joao", 'id_professor': 1},
    {'nome': "jose", 'id_professor': 2},
    {'nome': "maria", 'id_professor': 3}
]

alunos = [
    {'nome': "alexandre", 'id_aluno': 1},
    {'nome': "miguel", 'id_aluno': 2},
    {'nome': "janaina", 'id_aluno': 3},
    {'nome': "cicero", 'id_aluno': 4},
    {'nome': "dilan", 'id_aluno': 5}
]

disciplinas = [
    {'nome': "apis e microservicos", 'id_disciplina': 1, 'alunos': [1, 2, 3, 4], 'professores': [1], 'publica': False},
    {'nome': "matematica financeira", 'id_disciplina': 2, 'alunos': [2], 'professores': [3], 'publica': True},
    {'nome': "matematica basica", 'id_disciplina': 3, 'alunos': [1, 2], 'professores': [3, 2], 'publica': False}
]

class DisciplinaNaoEncontrada(Exception):
    def __init__(self, mensagem="Disciplina não encontrada."):
        super().__init__(mensagem)

class AlunoNaoEncontrado(Exception):
    def __init__(self, mensagem="Aluno não encontrado."):
        super().__init__(mensagem)

class ProfessorNaoEncontrado(Exception):
    def __init__(self, mensagem="Professor não encontrado."):
        super().__init__(mensagem)

# Funções para Professores
def listar_professores():
    return professores

def obter_professor(id_professor):
    for prof in professores:
        if prof['id_professor'] == id_professor:
            return prof
    raise ProfessorNaoEncontrado(f"Professor com id {id_professor} não encontrado.")

def criar_professor(dados):
    professores.append(dados)
    return dados

def atualizar_professor(id_professor, novos_dados):
    for i, prof in enumerate(professores):
        if prof['id_professor'] == id_professor:
            professores[i].update(novos_dados)
            return professores[i]
    raise ProfessorNaoEncontrado

def excluir_professor(id_professor):
    for i, prof in enumerate(professores):
        if prof['id_professor'] == id_professor:
            del professores[i]
            return True
    raise ProfessorNaoEncontrado



def listar_alunos():
    return alunos

def obter_aluno(id_aluno):
    for aluno in alunos:
        if aluno['id_aluno'] == id_aluno:
            return aluno
    raise AlunoNaoEncontrado(f"Aluno com id {id_aluno} não encontrado.")

def criar_aluno(dados):
    alunos.append(dados)
    return dados

def atualizar_aluno(id_aluno, novos_dados):
    for i, aluno in enumerate(alunos):
        if aluno['id_aluno'] == id_aluno:
            alunos[i].update(novos_dados)
            return alunos[i]
    raise AlunoNaoEncontrado

def excluir_aluno(id_aluno):
    for i, aluno in enumerate(alunos):
        if aluno['id_aluno'] == id_aluno:
            del alunos[i]
            return True
    raise AlunoNaoEncontrado



def listar_disciplinas():
    return disciplinas

def obter_disciplina(id_disciplina):
    for disc in disciplinas:
        if disc['id_disciplina'] == id_disciplina:
            return disc
    raise DisciplinaNaoEncontrada(f"Disciplina com id {id_disciplina} não encontrada.")

def criar_disciplina(dados):
    disciplinas.append(dados)
    return dados

def atualizar_disciplina(id_disciplina, novos_dados):
    for i, disc in enumerate(disciplinas):
        if disc['id_disciplina'] == id_disciplina:
            disciplinas[i].update(novos_dados)
            return disciplinas[i]
    raise DisciplinaNaoEncontrada

def excluir_disciplina(id_disciplina):
    for i, disc in enumerate(disciplinas):
        if disc['id_disciplina'] == id_disciplina:
            del disciplinas[i]
            return True
    raise DisciplinaNaoEncontrada



def leciona(id_professor, id_disciplina):
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada



def esta_matriculado(id_aluno, id_disciplina):
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_aluno in disciplina['alunos']
    raise DisciplinaNaoEncontrada

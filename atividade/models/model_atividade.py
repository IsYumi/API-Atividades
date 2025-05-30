from ..database import db

class AtividadeNaoEncontrada(Exception):
    pass

class Atividade(db.Model):
   __tablename__ = 'atividade'

   id = db.Column(db.Integer, primary_key=True)
   id_turma = db.Column(db.Integer,nullable=False)
   enunciado = db.Column(db.String,nullable=False)
   respostas = db.Column(db.ARRAY(db.String),nullable=False)

   def __init__(self,id,id_turma,enunciado,respostas):
      self.id = id
      self.id_turma = id_turma
      self.enunciado = enunciado
      self.respostas = respostas

   def to_dict(self):
    return {'id':self.id,'id_turma':self.id_turma,'enunciado':self.enunciado,'respostas':self.respostas}

def listar_atividades():
    atividades = Atividade.query.all()
    return [atividade.to_dict() for atividade in atividades]

def obter_atividade(id):
  atividade = Atividade.query.get(id)
  if not atividade:
        raise AtividadeNaoEncontrada
  return atividade.to_dict()


def criar_atividade(dados):
   nova_atividade = Atividade(id=dados['id'],id_turma=dados['id_turma'],enunciado=dados['enunciado'],respostas=dados['respostas'])
   db.session.add(nova_atividade)
   db.session.commit()
   return {'Mensagem':'Atividade adicionada!!'},201

def atualizar_atividade(id,novos_dados):
    atividade = Atividade.query.get(id)
    if atividade:
        atividade.id = novos_dados['id']
        atividade.id_turma = novos_dados['id_turma']
        atividade.enunciado = novos_dados['enunciado']
        atividade.respostas = novos_dados['respostas']
        db.session.commit()
        return {'Mensagem':'Atividade atualizada'}       
    raise AtividadeNaoEncontrada

def excluir_atividade(id):
   atividade = Atividade.query.get(id)
   if atividade:
      db.session.delete(atividade)
      db.session.commit()
      return {"Mensagem":'Atividade deletada!!'}
   raise AtividadeNaoEncontrada
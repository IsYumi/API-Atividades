activits = [
    {
        'id':1,
        'id_turma':101,
        'enunciado':'O que são planícies?',
        'respostas':[
            {'id_aluno':1,'resposta':'foto_resposta.png','nota':10},
            {'id_aluno':2,'resposta':'foto_resposta.png','nota':8.5}
        ]
},
    {
        'id':2,
        'id_turma':102,
        'enunciado':'Qual a diferença de figuras de linguagem e funções de linguagem?',
        'respostas':[
            {'id_aluno':1,'resposta':'resposta_linguagens.png','nota':7}
        ]
    }
]

class AtividadeNaoEncontrada(Exception):
    pass

def listar_atividades():
    return activits

def obter_atividade(id):
  for act in activits:
     if act['id'] == id:
        return act
  raise AtividadeNaoEncontrada


def criar_atividade(dados):
   activits.append(dados)
   return dados

def atualizar_atividade(id,novos_dados):
    for i,act in enumerate(activits):
        if act.get['id'] == id:
            act.update(novos_dados)
            return act
    raise AtividadeNaoEncontrada

def excluir_atividade(id):
   for i,act in enumerate(activits):
      if act.get['id'] == id:
         del activits[i]
         return True
   raise AtividadeNaoEncontrada
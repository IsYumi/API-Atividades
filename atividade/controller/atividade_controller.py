from flask import Blueprint,jsonify,request
from models import model_atividade
from clientes.pessoa_service_client import PessoaService

atividade_bp = Blueprint('atividade_bp',__name__)

@atividade_bp.route('/',methods=['GET'])
def listar_atividades():
    return jsonify(model_atividade.listar_atividades())

@atividade_bp.route('/<int:id_atividade>',methods=['GET'])
def buscar_atividade(id_atividade):
   try: 
    activity = model_atividade.obter_atividade(id_atividade) 
    return jsonify(activity)
   except model_atividade.AtividadeNaoEncontrada :
      return ({'Mensagem':'Atividade não encontrada'}),404

@atividade_bp.route('/<int:id_atividade>/docente/<int:id_docente>',methods=['GET'])
def obter_atividade_para_professor(id_atividade,id_professor):
    try:
       activity = model_atividade.obter_atividade(id_atividade)
       if not PessoaService.verifica_leciona(id_professor,activity['id_disciplina']):
          activity = activity.copy()
          activity.pop('respostas',None)
       return jsonify(activity)
    except model_atividade.AtividadeNaoEncontrada:
       return jsonify({'Erro':'Atividade não encontrada!'}),404
    
@atividade_bp.route('/',methods=['POST'])
def criar_nova_atividade():
   try:
      novos_dados = request.get_json()
      new_activity = model_atividade.criar_atividade(novos_dados)
      return jsonify(new_activity),201
   except model_atividade.AtividadeNaoEncontrada:
      return ({'Mensagem':'Erro na criação'}),500
   
@atividade_bp.route('/<int:id_atividade>',methods=['PUT'])
def atualizar_atividade(id_atividade):
   try:
      data_updated = request.get_json()
      activity_update =  model_atividade.atualizar_atividade(id_atividade,data_updated)
      if activity_update:
         return jsonify(activity_update),200
      else:
         return jsonify({'Mensagem':'Atividade não encontrada para ser atualizada!'}),404
   except model_atividade.AtividadeNaoEncontrada as e:
      return jsonify({'Mensagem':f'Erro de ao atualizar: {e}'}),500
   
@atividade_bp.route('/<int:id_atividade>',methods=['DELETE'])
def deletar_atividade(id):
   try:
      if model_atividade.excluir_atividade(id):
         return jsonify({'Mensagem':'Atividade deletada!!'}),204
      else:
         return jsonify({'Mensagem':'Atividade não encontrada para ser deletada!'}),404
   except model_atividade.AtividadeNaoEncontrada as e:
      return jsonify({'Mensagem':f'Erro ao deletar : {e}'}),500
from flask import Blueprint,jsonify,request
from ..models.model_atividade import (obter_atividade,listar_atividades,atualizar_atividade,excluir_atividade,criar_atividade,AtividadeNaoEncontrada)
from ..clientes.pessoa_service_client import PessoaService

atividade_bp = Blueprint('atividade_bp',__name__)

@atividade_bp.route('/',methods=['GET'])
def mostrar_atividades():
    return jsonify(listar_atividades())

@atividade_bp.route('/<int:id_atividade>',methods=['GET'])
def buscar_atividade(id_atividade):
   try: 
    activity = obter_atividade(id_atividade) 
    return jsonify(activity)
   except AtividadeNaoEncontrada :
      return ({'Mensagem':'Atividade não encontrada'}),404

@atividade_bp.route('/<int:id_atividade>/docente/<int:id_docente>',methods=['GET'])
def obter_atividade_para_professor(id_atividade,id_professor):
    try:
       activity = obter_atividade(id_atividade)
       if not PessoaService.verifica_leciona(id_professor,activity['id_disciplina']):
          activity = activity.copy()
          activity.pop('respostas',None)
       return jsonify(activity)
    except AtividadeNaoEncontrada:
       return jsonify({'Erro':'Atividade não encontrada!'}),404
    

@atividade_bp.route('/',methods=['POST'])
def criar_nova_atividade():
   try:
      novos_dados = request.get_json()
      new_activity = criar_atividade(novos_dados)
      return jsonify(new_activity),201
   except AtividadeNaoEncontrada:
      return ({'Mensagem':'Erro na criação'}),500
   
@atividade_bp.route('/<int:id_atividade>',methods=['PUT'])
def atualizar_atividade_rota(id_atividade):
   try:
      data_updated = request.get_json()
      if data_updated is None:
         return jsonify({'Mensagem':'JSON inválido ou ausentes'}),400
      activity_update =  atualizar_atividade(id_atividade,data_updated)
      
      return jsonify(activity_update),200
   
   except AtividadeNaoEncontrada as e:
      return jsonify({'Mensagem':f'Erro de ao atualizar: {e}'}),500
   
@atividade_bp.route('/<int:id_atividade>',methods=['DELETE'])
def remover_atividade(id_atividade):
   try:
      if excluir_atividade(id_atividade):
         return jsonify({'Mensagem':'Atividade deletada!!'}),204
   except  AtividadeNaoEncontrada:
         return jsonify({'Mensagem':'Atividade não encontrada para ser deletada!'}),404
   except Exception  as e:
      return jsonify({'Mensagem':f'Erro ao deletar : {str(e)}'}),500
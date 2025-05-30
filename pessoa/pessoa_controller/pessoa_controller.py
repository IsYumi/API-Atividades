from flask import Blueprint, jsonify, request
from models import pessoa_model


pessoa_bp = Blueprint('pessoa_bp', __name__)


@pessoa_bp.route('/professores', methods=['GET'])
def listar_professores():
    professores = pessoa_model.listar_professores()
    return jsonify(professores)


@pessoa_bp.route('/professores/<int:id_professor>', methods=['GET'])
def obter_professor(id_professor):
    try:
        professor = pessoa_model.obter_professor(id_professor)
        return jsonify(professor)
    except pessoa_model.ProfessorNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.get_json()
    professor = pessoa_model.criar_professor(dados)
    return jsonify(professor), 201


@pessoa_bp.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    dados = request.get_json()
    try:
        professor = pessoa_model.atualizar_professor(id_professor, dados)
        return jsonify(professor)
    except pessoa_model.ProfessorNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
def excluir_professor(id_professor):
    try:
        pessoa_model.excluir_professor(id_professor)
        return jsonify({'mensagem': 'Professor excluído com sucesso.'})
    except pessoa_model.ProfessorNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404



@pessoa_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = pessoa_model.listar_alunos()
    return jsonify(alunos)


@pessoa_bp.route('/alunos/<int:id_aluno>', methods=['GET'])
def obter_aluno(id_aluno):
    try:
        aluno = pessoa_model.obter_aluno(id_aluno)
        return jsonify(aluno)
    except pessoa_model.AlunoNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()
    aluno = pessoa_model.criar_aluno(dados)
    return jsonify(aluno), 201


@pessoa_bp.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    dados = request.get_json()
    try:
        aluno = pessoa_model.atualizar_aluno(id_aluno, dados)
        return jsonify(aluno)
    except pessoa_model.AlunoNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def excluir_aluno(id_aluno):
    try:
        pessoa_model.excluir_aluno(id_aluno)
        return jsonify({'mensagem': 'Aluno excluído com sucesso.'})
    except pessoa_model.AlunoNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor, id_disciplina):
    try:
        leciona = pessoa_model.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except pessoa_model.DisciplinaNaoEncontrada as e:
        return jsonify({'erro': str(e)}), 404


@pessoa_bp.route('/matriculado/<int:id_aluno>/<int:id_disciplina>', methods=['GET'])
def verificar_matricula(id_aluno, id_disciplina):
    try:
        matriculado = pessoa_model.esta_matriculado(id_aluno, id_disciplina)
        return jsonify({'matriculado': matriculado})
    except pessoa_model.DisciplinaNaoEncontrada as e:
        return jsonify({'erro': str(e)}), 404
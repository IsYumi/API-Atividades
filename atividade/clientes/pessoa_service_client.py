import requests as r

url_pessoa_service = 'http://127.0.0.1:5000/api/docentes'

class PessoaService:
    @staticmethod
    def verifica_leciona(id_professor,id_disciplina):
        url= f'{url_pessoa_service}/leciona/{id_professor}/{id_disciplina}'
        try:
            response = r.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('leciona',False) if data.get('isok') else False
        except r.RequestException as erro:
            print(f'Erro ao acessar pessoa_service : {erro}')
            return False
        
    @staticmethod
    def obter_docente_id(id_docente):
        url = f'{url_pessoa_service}/docente/{id_docente}'
        try:
            response = r.get(url)
            response.raise_for_status()
            return response.json()
        except r.exceptions.RequestException as e:
            print(f'Erro ao procurar docente com id {id_docente}: {e}')
            return None

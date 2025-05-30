import requests as r

url_pessoa_service = ''

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
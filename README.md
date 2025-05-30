# API-Atividades📚
API para Atividades do Projeto Gestão Escolar

## Tecnologias utilizadas🚀
- Flask
- Python 3.x
- SQLAlchemy(Uso para Banco de dados)
- Biblioteca requests(Consumo da api externa)

## Sobre o projeto📕
Esta API tem como objetivo gerenciar informações de Professores, Alunos, Disciplinas e suas relações. Permite criar, consultar, atualizar e deletar registros, além de controlar a vinculação de alunos e professores às disciplinas

## Estrutura do Projeto📄
```
├── API-ATIVIDADES/
│   ├── atividade/
│   │   ├── clientes/
│   │   │   └── pessoa_service_client.py
│   │   ├── controller/
│   │   │   └── atividade_controller.py
│   │   ├── models/
│   │   │   ├── model_atividade.py
│   │   │   └── init.py
│   │   ├── app.py
│   │   ├── config.py
│   │   └── database.py
│   ├── instance/
│   │   └── atividade.db
│   ├── pessoa/
│   │   ├── controllers/
│   │   ├── database/
│   │   │   └── database.py
│   │   ├── model/
│   │   │   └── model.py
│   │   ├── app.py
│   │   ├── config.py
│   │   └── dockerfile.txt
│   ├── venv/
│   └── README.md


```

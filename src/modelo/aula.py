from flask_restx import fields
from src.server.instance import api

aula_request = api.model('Requisição Aula', {
    'nome': fields.String(description="Nome ou disciplina da aula.", min_length=1, max_length=45, required=True),
    'quantidade_alunos': fields.Integer(description="Quantidade de alunos presentes na aula.", required=True),
    'inicio': fields.String(description='Data de inicio da aula. Deve ser no formato yyyy/mm/dd hh:mm:ss', required=True, 
        example='2022/06/05 15:00:00'),
    'fim': fields.String(description='Data de finalização da aula. Deve ser no formato yyyy/mm/dd hh:mm:ss', required=True,
        example='2022/06/05 18:00:00'),
    'sala_id': fields.Integer(description='ID da sala onde ocorrerá a aula.', required=True)
})

aula_response = api.model('Aula', {
    'id': fields.Integer(description="ID da aula."),
    'nome': fields.String(description="Nome ou disciplina da aula."),
    'quantidade_alunos': fields.Integer(description="Quantidade de alunos presentes na aula."),
    'inicio': fields.String(description='Data de inicio da aula.'),
    'fim': fields.String(description='Data de finalização da aula.'),
    'sala_id': fields.Integer(description='ID da sala onde ocorrerá a aula.')
})


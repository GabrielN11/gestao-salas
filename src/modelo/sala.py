from flask_restx import fields
from src.server.instance import api

from src.modelo.aula import aula_response
from src.modelo.resposta import sucesso_response

sala_request = api.model('Requisição Sala', {
    'nome': fields.String(description="Nome da sala de aula.", min_length=1, max_length=45, required=True),
    'capacidade': fields.Integer(description="Capacidade máxima de alunos na sala.", required=True),
})

sala_response_model = api.model('Sala', {
    'id': fields.Integer(description='ID da sala de aula.'),
    'nome': fields.String(description="Nome da sala de aula"),
    'capacidade': fields.Integer(description="Capacidade máxima de alunos na sala"),
    'aulas': fields.List(fields.Nested(aula_response))
})

sala_response = api.inherit('Resposta', sucesso_response, {
    'response': fields.List(fields.Nested(sala_response_model, allow_null=True))
})


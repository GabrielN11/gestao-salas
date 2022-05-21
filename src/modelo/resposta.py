from flask_restx import fields
from src.server.instance import api

sucesso_response = api.model('Sucesso', {
    'message': fields.String()
})

erro_response = api.model('Erro', {
    'error': fields.String()
})
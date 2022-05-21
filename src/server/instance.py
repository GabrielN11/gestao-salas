from flask_restx import Api
from flask import Flask
from flask_cors import CORS

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        cors = CORS(self.app, resources={r'*': {'origins': '*'}})
        CORS(self.app)
        self.api = Api(self.app, 
            version='1.0',
            title='Cadastro de Salas',
            description='Uma API para gestão de salas de aula.',
            doc='/docs'
        )

    def run(self):
        self.app.run(debug=True)


server = Server()
api = server.api

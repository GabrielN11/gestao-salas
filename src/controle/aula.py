#Livrarias
from datetime import datetime
from flask import request
from flask_restx import Resource

#Modulos
from src.server.instance import api
from src.dao.aulaDao import AulaDAO
from src.dao.salaDao import SalaDAO
from src.utils.conversaoDatas import ConversaoDatas

#Documentação
from src.modelo.aula import aula_request
from src.modelo.resposta import sucesso_response, erro_response

#Rotas

@api.route('/agendar-aula')
class Aula(Resource):

    #Decorators de documentação
    @api.expect(aula_request, validate=True, code=201)
    @api.response(201, 'Sucesso', sucesso_response)
    @api.response(400, 'Erro', erro_response)
    @api.response(500, 'Erro', erro_response)
    def post(self):
        #Criando objetos necessários
        aulaDao = AulaDAO()
        salaDao = SalaDAO()
        conversaoDatas = ConversaoDatas()

        #Dados do post
        dados = api.payload
        nome = dados['nome']
        inicio = dados['inicio']
        fim = dados['fim']
        salaId = dados['sala_id']

        #Validações
        try:
            qtdAlunos = int(dados['quantidade_alunos'])
            if(qtdAlunos < 1):
                return {"error": "Quantidade de alunos precisa ser maior do que zero."}, 400
        except:
            return {"error": "Quantidade de alunos precisa ser um valor inteiro."}, 400

        if nome == '':
            return {"error": "Nome da aula não foi informado."}, 400

        if len(inicio) < 19 or len(inicio) > 19:
            return {"error": "Formato da data de início incorreto. A data precisa ser passada no seguinte formato: yyyy/mm/dd hh:mm:ss"}, 400
        if len(fim) < 19 or len(inicio) > 19:
            return {"error": "Formato da data de finalização incorreto. A data precisa ser passada no seguinte formato: yyyy/mm/dd hh:mm:ss"}, 400

        if salaId == '':
            return {"error": "ID da sala de aula não foi informado."}

        #Conferindo se a sala está disponível durante o período através de uma consulta SQL
        aulasConflitantes = aulaDao.listarDisponobilidade(inicio, fim, salaId)
        #Case haja uma aula durante os horários, a a tupla será maior do que 0
        if len(aulasConflitantes) > 0:
            return {"error": "A sala de aula já está ocupada durante este período."}, 400

        #Checando se a sala suporta a quantidade de alunos
        try:
            sala = salaDao.selecionarPorId(salaId)[0]
        except:
            return {"error": "Sala não encontrada."}, 400

        if sala[2] < qtdAlunos:
            return {"error": "A sala não suporta a quantidade de alunos."}, 400

        #Convertendo datas para datetime e checando se não estão corretas
        inicioDatetime = conversaoDatas.paraDatetime(inicio)
        fimDatetime = conversaoDatas.paraDatetime(fim)
        if inicioDatetime < datetime.now():
            return {"error": "Data inválida. A data informada já se passou."}
        if inicioDatetime >= fimDatetime:
            return {"error": "A data de início é maior ou igual à data de finalização."}, 400

        #Cadastro no banco de dados
        try:
            aulaDao.criar(nome, qtdAlunos, inicio, fim, salaId)
            return {"message": f"Aula '{nome}' foi agendada com sucesso para {conversaoDatas.paraString(inicioDatetime)} na sala '{sala[1]}'."}, 201
        except Exception as err:
            return {"error": 'Ocorreu um erro durante o agendamento da aula.'}, 500
        



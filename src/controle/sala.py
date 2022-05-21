#Livrarias
from flask import request
from flask_restx import Resource

#Modulos
from src.server.instance import api
from src.dao.salaDao import SalaDAO
from src.dao.aulaDao import AulaDAO
from src.utils.conversaoDict import ConversaoDicionario

#Documentação
from src.modelo.sala import sala_request, sala_response
from src.modelo.resposta import erro_response, sucesso_response

#Rotas

@api.route('/sala')
class Sala(Resource):
    
    #Decorators de documentação
    @api.expect(sala_request, validate=True)
    @api.response(200, 'Sucesso', sucesso_response)
    @api.response(400, 'Erro', erro_response)
    @api.response(500, 'Erro', erro_response)
    def post(self):
        salaDao = SalaDAO()

        dados = api.payload
        nome = dados['nome']

        #Validações
        try:
            capacidade = int(dados['capacidade'])
        except:
            return { "error": 'Capacidade precisa ser um valor inteiro.' }, 400
        
        if nome == '':
            return { "error": 'É necessário informar um nome para sala.' }, 400

        #Acesso ao banco de dados
        try:
            salaDao.criar(nome, capacidade)
            return { "message": f"Sala '{nome}' registrada com sucesso." }, 201
        except Exception as err:
            return {
                "error": 'Ocorreu um erro durante o cadastro da sala.'
            }, 500


    #Decorators de documentação
    @api.doc(params={"disponiveis": {'description': "Retornar apenas salas livres.", 'type': 'Boolean'},
     "pesquisa": "Pesquisar pelo nome de uma sala."})
    @api.marshal_with(sala_response)
    @api.response(400, 'Erro', erro_response)
    @api.response(500, 'Erro', erro_response)
    def get(self):
        salaDao = SalaDAO()
        aulaDao = AulaDAO()
        conversaoDicionario = ConversaoDicionario()

        pesquisa = None
        apenasDisponiveis = None

        if request.args.get('pesquisa'):
            pesquisa = request.args.get('pesquisa').lower()
        if request.args.get('disponiveis'):
            apenasDisponiveis = request.args.get('disponiveis')

        try:
            salas = salaDao.listarTodas()
            
            #Função para selecionar as aulas de cada sala e formatar para dicionário
            def listarAulasEFormatar(sala):
                aulas = aulaDao.listarPorSala(sala[0])
                aulas = list(map(lambda aula: conversaoDicionario.aula(aula), aulas))
                sala = conversaoDicionario.sala(sala)
                sala['aulas'] = aulas
                return sala
            salas = list(map(listarAulasEFormatar, salas))

            #Checando se foram passados filtros de pesquisa
            if pesquisa or apenasDisponiveis:
                #Função para filtrar de acordo com os parâmetros passados
                def filtrar(sala):
                    if pesquisa and apenasDisponiveis:
                        return True if (sala['nome'].lower().__contains__(pesquisa) and len(sala['aulas']) == 0) else False
                    elif pesquisa:
                        return True if sala['nome'].lower().__contains__(pesquisa) else False
                    else:
                        return True if len(sala['aulas']) == 0 else False
                salas = list(filter(filtrar, salas))

            resposta = salas
            mensagem = 'Listado com sucesso' if len(resposta) >= 1 else "Não foram encontradas salas"

            return {
                "message": mensagem,
                "response": resposta
            }, 200
        except Exception as err:
            return {"error": 'Ocorreu um erro durante a consulta das salas.'}




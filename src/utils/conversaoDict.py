from src.utils.conversaoDatas import ConversaoDatas

#Classe que converte as tuplas vindas do pymysql em dicionários mais legíveis
class ConversaoDicionario:
    def __init(self):
        pass

    def aula(self, tupla):
        conversaoDatas = ConversaoDatas()
        inicioStr = conversaoDatas.paraString(tupla[3])
        fimStr = conversaoDatas.paraString(tupla[4])
        return {
            "id": tupla[0],
            "nome": tupla[1],
            "quantidade_alunos": tupla[2],
            "inicio": inicioStr,
            "fim": fimStr,
            "sala_id": tupla[5]
        }

    def sala(self, tupla):
        return {
            "id": tupla[0],
            "nome": tupla[1],
            "capacidade": tupla[2]
        }
from src.dao.dao import DAO

class AulaDAO(DAO):
    def criar(self, nome, qtdAlunos, inicio, fim, salaId):
        sql = f"""
                INSERT INTO aula (nome, quantidade_alunos, inicio, fim, sala_id) 
                VALUES ('{nome}', {qtdAlunos}, '{inicio}', '{fim}', {salaId});
            """
        return self.executar(sql)
            

    def atualizar(self, nome, qtdAlunos, inicio, fim, id):
        sql = f"""
                UPDATE aula SET nome = {nome}, quantidade_aluno = {qtdAlunos}, 
                inicio = {inicio}, fim = {fim} WHERE aula_id = {id};
            """
        self.executar(sql)

    def listarDisponobilidade(self, inicio, fim, salaId):
        sql = f"""
            SELECT aula.id_aula, sala.id_sala FROM aula INNER JOIN sala ON sala.id_sala = aula.sala_id  
            WHERE (fim BETWEEN '{inicio}'  AND '{fim}' OR inicio BETWEEN '{inicio}' AND '{fim}') AND  (aula.sala_id = {salaId});
        """

        return self.executar(sql)

    def listarPorSala(self, salaId):
        sql = f"""
            SELECT id_aula, nome, quantidade_alunos, inicio, fim, sala_id FROM aula WHERE sala_id = {salaId};
        """

        return self.executar(sql)

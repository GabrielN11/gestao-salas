from src.dao.dao import DAO

class SalaDAO(DAO):
    def criar(self, nome, capacidade):
        sql = f"""
            INSERT INTO sala (nome, capacidade) 
            VALUES ('{nome}', {capacidade});
        """
        self.executar(sql)

    def listarTodas(self):
        sql = f"""
            SELECT id_sala, nome, capacidade FROM sala;
        """
        return self.executar(sql)

    def selecionarPorId(self, id):
        sql = f"""
            SELECT id_sala, nome, capacidade FROM sala WHERE id_sala = {id};
        """
        return self.executar(sql)
    

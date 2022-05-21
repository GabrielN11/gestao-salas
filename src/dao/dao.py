from src.lib.mysql import mysql
from pymysql import MySQLError

class DAO:
    def executar(self, sql):
        try:
            with mysql as bd:
                cursor = bd.conn.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                bd.conn.commit()
            return result
        except MySQLError as err:
            print(str(err))
            raise MySQLError('Erro ao acessar banco de dados.')
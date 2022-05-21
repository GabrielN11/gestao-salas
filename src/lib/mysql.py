import pymysql
import env

class MySqlCon:
    def __init__(self,
        user=env.user,
        password=env.password,
        host=env.host,
        database=env.database
    ):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.conn = None

    def __enter__(self):
        self.criarConexao()
        return self

    def __exit__(self, type, value, traceback):
        self.conn.close()

    def criarConexao(self):
        try:
            self.conn = pymysql.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
        except pymysql.DatabaseError as err:
            print(err)

mysql = MySqlCon()
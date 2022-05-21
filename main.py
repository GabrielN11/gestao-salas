#Instância do servidor
from src.server.instance import server


#Rotas

from src.controle.sala import Sala
from src.controle.aula import Aula


if __name__ == "__main__":
    server.run()
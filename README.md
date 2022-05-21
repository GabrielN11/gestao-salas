# Gestão de Salas 1.0

## O que é?
Se trata de uma API para gerir salas de aula e suas respectivas disciplinas, podendo cadastrar salas de aula e agendar aulas específicas para estas salas em um período determinado. A API permite agendar as aulas em salas previamente cadastradas desde que a sala não esteja ocupada durante o período determinado para aula. A capacidade de pessoas em cada sala é requisitada, assim como a quantidade de alunos em cada aula, evitando assim conflitos em relação à lotação.

## Tecnologias utilizadas

- Python 3
- MySQL
- Flask
- Flask_restx
- PyMySQL
- Swagger

## Como usar?

### Antes de tudo...

É necessário ter instalado o **Python 3** e seu instalador de pacotes **pip**, além do **virtualenv** para se criar o ambiente virtual do projeto. O virtualenv pode ser instalado através do pip com o seguinte comando:

`pip install virtualenv`

Além disso, será necessário o **MySQL** instalado para que o banco de dados funcione. É recomendado também ter instalado o **MYSQL Workbench** para facilitar na execução do script .sql que irá criar o banco de dados.

### Preparando a API

Clone este repositório para uma pasta de sua preferência, depois disso abra o terminal na pasta raiz do projeto e crie um ambiente virtual com o comando:

`virtualenv gestao-aulas`

Será criada um diretório **gestao-aulas** no diretório da API, após isso, ainda na pasta raiz pelo terminal, inicialize o ambiente virtual com o comando:

`source gestao-aulas/bin/activate`

No Windows pode ser necessário usar o comando `source gestao-aulas/Scripts/activate`

Com o ambiente virtual inicilizado, é hora de instalar as dependências do projeto listadas no arquivo **requirements.txt**, para fazer isso, basta digitar o seguinte comando no terminal na raiz do projeto:

`pip install -r requirements.txt`

O pip deve instalar todas as dependências do projeto, como Flask e Flask_restx e estamos quase prontos para executar a API.

### Preparando o Banco de Dados

Há um arquivo **database.sql** na pasta raiz do projeto, nele há os comandos SQL necessários para criar o banco de dados. Você pode usar o MySQL Workbench para executar o script automaticamente, basta entrar na sua conexão, no menu superior esquerdo clicar em:

`File > Run SQL Script > Selecionar o arquivo database.sql... > Run`

Com isso o banco de dados será criado, você pode confirmar checando os schemas no seu MySQL Workbench e verificar se há um novo banco de dados chamado **gestao_salas**.

Você também pode copiar o script de dentro do arquivo e executá-lo manualmente caso prefira.

Após criar o banco de dados, volte a pasta raiz da API e crie um arquivo **env.py**, é onde serão armazenadas as variáveis de ambiente necessárias para o PyMySQL acessar o banco de dados. Dentro deste arquivo, você deve colocar as informações de acesso ao seu banco de dados MySQL, como usuário, senha e porta. Siga o modelo a seguir para criar essas variáveis:

```python
user = 'user'
password = 'senhaaqui'
host = 'localhost'
port = 3306
database = 'gestao_salas'
```

## Executando a API

Depois de concluir as etapas acima, basta executar o arquivo **main.py** na pasta raiz da API para começar a rodar.

`python main.py`

A API irá rodar na URL `http://127.0.0.1:5000`, mas cheque o terminal para ter certeza que sua URL não será diferente.

## Documentação

Você pode checar a documentação da API para obter detalhes de como usá-la, quais requisições enviar para criar as salas de aula e agendamentos, além de listar as salas. A documentação foi feita com Swagger, incluído na biblioteca Flask_restx, e através dele você pode conferir as entradas de cada rota, as saídas e também pode testá-la sem ser necessário instalar outros programas, como Postman.

Após iniciar a API, acesse a URL da API na rota **/docs** no seu navegador para conferir a documentação.

`http://127.0.0.1:5000/docs`


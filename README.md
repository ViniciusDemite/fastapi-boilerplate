# Boilerplate FastAPI

O propósito do projeto é a criação de um **boilerplate** para projetos que serão feitos utilizando o framework **FastAPI**, baseado no próprio [esquema da documentação](https://fastapi.tiangolo.com/tutorial/bigger-applications/) com alguns ajustes pessoais.

## Sumário

- [Instalação](#instalação)
  - [Configurações](#configurações)
  - [Verificando o projeto](#verificando-o-projeto)
  - [Executando o projeto](#executando-o-projeto)
- [Documentações](#documentações)

## Instalação

Esse projeto utiliza o Docker e Docker Compose para facilitar a usabilidade. Para fazer rodar o projeto antes é necessário alterar algumas configurações sobre o projeto.

### Configurações

As configurações abaixo são referentes ao arquivo **docker-compose.yml**:

- Nas variáveis **container_name** alterar para o nome desejado de cada container (opcional)
- Gerar um nova senha para as variáveis **MYSQL_ROOT_PASSWORD** e **MYSQL_PASSWORD**
  - Crie uma por conta ou utilize o método `openssl rand -hex 32`
- Alterar o nome do banco de dados na variável **MYSQL_DATABASE**

As configurações abaixo se referem à variável de ambiente **.env**:

- Faça uma cópia do arquivo [.env.sample](./app/.env.sample) com o nome de **.env**
- Para as chaves utilize o comando `openssl rand -hex 32` para gerar um chave única

### Executando o projeto

Após fazer as configurações necessárias para rodar o projeto utilize o comando: `docker compose up -d`.

### Verificando o projeto

Após executar o Docker sem erros é possível verificar a integridade do projeto ao acessar [localhost](http://localhost:8000).
Caso queira verificar/interagir com o banco de dados, com os containers rodando, execute o comando:

- `docker compose exec db bash` para ter acesso ao bash para poder acessar o banco.
  - Execute o comando: `mysql -h localhost -u root -p` e informe a senha do **usuário root**.

Para verificar o projeto acesse em:

## Documentações

- [FastAPI](https://fastapi.tiangolo.com/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [Python Jose](https://github.com/mpdavis/python-jose)
- [Passlib](https://passlib.readthedocs.io/en/stable/)

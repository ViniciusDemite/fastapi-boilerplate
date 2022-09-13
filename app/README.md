# Sumário

- [Estrutura do projeto](#estrutura-do-projeto)
  - [Controladores](#controladores)
  - [Modelos](#modelos)
  - [Rotas](#rotas)
  - [Esquemas](#esquemas)
  - [Arquivo principal](#arquivo-principal)
- [Variáveis de ambiente](#env-variables)
  - [JWT](#jwt)

## Estrutura do projeto

Aqui se encontra uma explicação mais detalhada sobre a estrutura do projeto para fins de facilidade de navegação e novas implementações.

### Controladores

Na pasta [controllers](./controllers/) está definida a lógica das funções presentes em rotas.

### Modelos

Na pasta [models](./models/) está definidos os modelos da base de dados.

### Rotas

Na pasta [routers](./routers/) estão organizadas as rotas principais do projeto, podendo estar dividia em vários módulos ou um módulo único.

### Esquemas

Na pasta [schemas](./schemas/) estão definidos os schemas (modelos) a serem usados pelas rotas de API para recebimento, envio e base de dados.

### Arquivo principal

O arquivo principal do projeto é o **main.py** onde se encontra as configurações necessárias para a execução do projeto.

## <a name="env-variables"></a>Variáveis de ambiente

As variáveis de ambiente, representadas pelo arquivo [.env.sample](./.env.sample), são necessárias para as configurações mais sigilosas da aplicação. Abaixo temos explicação sobre elas:

---

### JWT

- **JWT_SECRET_KEY** chave secreta para fazer as operações com o toke JWT
  - Normalmente criada pelo comando: `openssl rand -hex 32`
- **HASH_ALGORITHM** é o algorítimo utilizado na criação do token
  - Por padrão está definida como **HS256**, mas se quiser pode mudar para **RS256** ([referência](https://auth0.com/blog/rs256-vs-hs256-whats-the-difference/))
- **ACCESS_TOKEN_EXPIRATION_MINUTES** tempo, em minutos, que será válido o token

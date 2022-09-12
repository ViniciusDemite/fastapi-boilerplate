# Sumário

- [Estrutura do projeto](#estrutura-do-projeto)
  - [Controladores](#controladores)
  - [Modelos](#modelos)
  - [Rotas](#rotas)
  - [Esquemas](#esquemas)
  - [Arquivo principal](#arquivo-principal)

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

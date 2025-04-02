# DockerFile - Projeto Python com Flask

Este repositório contém um Dockerfile para construir e rodar uma aplicação Python simples utilizando o framework **Flask**. O objetivo é demonstrar como configurar um ambiente de desenvolvimento em contêineres Docker para rodar uma aplicação Python.

## Pré-requisitos

Antes de começar, você precisa ter o seguinte instalado:

- [Docker](https://www.docker.com/) - Para construir e rodar o contêiner.
- [Git](https://git-scm.com/) - Para clonar o repositório.

## Como rodar o projeto

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/Mingau1009/DockerFile.git
cd DockerFile

Dentro da pasta do projeto, construa a imagem Docker com o seguinte comando:
docker build -t banco .

Após a contrução você pode rodar o container com o seguinte comando:
docker run -p 3000:3000 banco

###Testando a aplicação

Agora, com o contêiner rodando, você pode testar a aplicação acessando a URL no seu navegador ou utilizando uma ferramenta como o Postman ou curl.

GET: Acesse http://localhost:3000/usuario/(id de sua escolha) no seu navegador ou execute o seguinte comando no cmd:
curl http://localhost:3000/(id de sua escolha)

POST: Envie uma requisição POST para a rota /data com um JSON no corpo da requisição. Exemplo de requisição com o curl:
curl -X POST http://localhost:3000/usuario -H "Content-Type: application/json" -d "{\"email\":\"suaescolha\",\"name\":\"suaescolha\",\"senha\":\"suaescolha\"}"

A resposta será parecida com essa:
{
  "email": "joao@exemplo.com",
  "nome": "João da Silva",
  "senha": "senha123"
}




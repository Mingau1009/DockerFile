FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as dependências diretamente no sistema
RUN pip install --no-cache-dir flask flask-jwt-extended marshmallow

# Expõe a porta 5000
EXPOSE 3000

# Define a variável de ambiente para desativar o modo de depuração do Flask
ENV FLASK_ENV=production
ENV FLASK_APP=api.py

# Comando para rodar a aplicação
CMD ["python", "api.py"]

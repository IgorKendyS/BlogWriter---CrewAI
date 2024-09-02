# Use uma imagem base Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta usada pela aplicação Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api:app"]

# Usa imagem Python como base
FROM python:3.11-slim

# Evita logs com buffer
ENV PYTHONUNBUFFERED=1

# Cria pasta e define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala os pacotes
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expondo porta para acesso ao Jupyter Notebook
EXPOSE 8888

# Comando para rodar Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]

# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o requirements.txt e instale as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . /app/

# Exponha a porta do servidor Django (8000)
EXPOSE 8000

# Defina variáveis de ambiente para o Django, exceto a senha
ENV DJANGO_SETTINGS_MODULE=projetoIntegrador.settings \
    DJANGO_SUPERUSER_USERNAME=dalpiaz \
    DJANGO_SUPERUSER_EMAIL=gabriel666dalpiaz@gmail.com \
    DJANGO_SUPERUSER_PASSWORD=admin

# Executar migrações e criar superusuário sem senha
RUN python manage.py migrate \
    && python manage.py createsuperuser --noinput || true

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

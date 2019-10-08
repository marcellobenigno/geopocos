# 1. INSTALAÇÃO

### Criação do Banco de Dados Espaciais:

``` bash
createdb geopocos
psql geopocos
# no banco, Habilitar a extensão PostGIS:
CREATE EXTENSION postgis;
\q
```

### Criação do Projeto:

``` bash
python -V
# ➜ Python 3.7.4

which python
# ➜ /Users/marcello/.pyenv/shims/python

# pasta do projeto:
cd ~/code 
mkdir geopocos
cd geopocos

# criando uma virtualenv para o projeto:
python -m venv .venv

# habilitando:
source .venv/bin/activate

which python
# ➜ /Users/marcello/code/geopocos/.venv/bin/python
```

### Instalando o Django:

``` bash
pip install django
# com o comando abaixo criamos o projeto django no diretório atual:
django-admin startproject geopocos .
```

💡 Para aumentar a produtividade, crie atalhos no terminal, no `~/.bashrc` ou no `~/.zshrc`:

```shell
# Python/Django
alias venv="python -m venv .venv && ve"
alias ve="source .venv/bin/activate"
alias m='python $VIRTUAL_ENV/../manage.py'
alias mmm='m makemigrations'
alias mm='m migrate'
```

### Configuração do settings.py:

Antes de configurar o arquivo `settings.py`, vamos instalar inicialmente três pacotes necessários para o nosso projeto:

```bash
pip install python-decouple psycopg2 dj-database-url
```

```python
# Após o import os:
from decouple import config, Csv
from dj_database_url import parse as db_url 


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# Application definition

# Modificações no INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # GeoDjango
    'django.contrib.gis',
    # My apps
]
# Modificações no DATABASES
DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
```

💡 Não se esqueça de criar um arquivo com todas as dependências do projeto e a cada vez que um novo pacote for adicionado.

```bash
pip freeze > requirements.txt
```

### Verificando o funcionamento do Django

```bash
# Para criar as tabelas no nosso banco de dados:
python manage.py migrate

# Para ver o projeto rodando:
python manage.py runserver
```
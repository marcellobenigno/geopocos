# GEOPOÇOS - 🌵 GeoDjango Unchained 🌵

Projeto apresentado na Live de Python do Canal **Geocast Brasil**.

![GeoDjango Unchained](docs/.pastes/2019-10-06-07-49-37.png)

## ÍNDICE DA APRESENTAÇÃO:

1. [SOBRE O INSTRUTOR](docs/01-apresentacao.md)
2. [INSTALAÇÃO](docs/02-instalacao.md)
3. [HELLO WORLD](docs/03-hello_world.md)
4. [USANDO O BOOTSTRAP COM HERANÇA DE TEMPLATES](docs/04-heranca-de-templates.md)
5. [NOSSO PRIMEIRO MAPA](docs/05-nosso-primeiro-mapa.md)
6. [MODELS](docs/06-models.md)
7. [ADICIONANDO OS POÇOS NO MAPA](docs/07-adicionando-pocos-mapa.md)
8. [CRIANDO O MAPA DE INTENSIDADE DE PONTOS (HEATMAP)](docs/08-adicionado-heatmap.md)


## REQUISITOS
* Python 3+ (de preferência o Python 3.7.4)
* PostgreSQL >= 10
* PostGIS >= 2.5.0
* GDAL, no linux instale com: `apt-get install python-gdal`. Se for mac um `brew install gdal` é suficiente.

## CONFIGURAÇÕES DO BANCO DE DADOS ESPACIAIS

É necessário criar um banco **PostgreSQL** e habilitar a extensão espacial **PostGIS**, no terminal, faça:

```
createdb geopocos
psql geopocos
CREATE EXTENSION postgis;
\d
```

## COMO DESENVOLVER?

* Clone o repositório;
* Crie um virtualenv com Python 3.7.4;
* Ative o virtualenv;
* Instale as dependências do ambiente de desenvolvimento;
* Crie o banco de dados espacial como foi descrito acima.


```
git clone https://github.com/marcellobenigno/geopocos.git
cd geopocos
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

* Renomeie o arquivo `env-sample` para `.env`:

```
mv env-sample .env
```

* Preencha as informações do `.env` e rode os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
```

* Adicione os registros nas duas tabelas:

```
python manage.py loaddata poco
python manage.py loaddata municipio
```


* Rode o `runserver`...

```
python manage.py runserver
```

...e verifique se o mapa abaixo é exibido no link **mapa**:

![](docs/.pastes/2019-10-07-21-58-05.png)
# django-full-template

This is a example of complete project made with Django, Django REST framework and render template.

The goal is to have a complete structure and consist of both rendering templates and REST API.

## This project was done with:

* [Python 3.9.8](https://www.python.org/)
* [Django 3.2.9](https://www.djangoproject.com/)
* [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-full-template.git
cd django-full-template
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

Este é um exemplo de um projeto completo feito com Django, Django REST framework and render template.

O objetivo é ter uma estrutura completa e consisa tanto para render templates quanto para API REST.

## Este projeto foi feito com:

* [Python 3.9.8](https://www.python.org/)
* [Django 3.2.9](https://www.djangoproject.com/)
* [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-full-template.git
cd django-full-template
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```
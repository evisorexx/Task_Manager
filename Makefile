PORT ?= 10000

install:
	poetry install

dev:
	python3 manage.py runserver

makemig:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

lint:
	poetry run flake8 --ignore=E501 task_manager

dotr:
	django-admin makemessages --ignore="static" --ignore=".env"  -l ru

savetr:
	django-admin compilemessages

tests:
	poetry run python3 manage.py test

start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

deploy:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi
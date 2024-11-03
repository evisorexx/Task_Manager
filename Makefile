PORT ?= 10000

install:
	poetry install

dev:
	python3 manage.py runserver

lint:
	poetry run flake8 --ignore=E501 task_manager

start:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi
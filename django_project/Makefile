HOST ?= 0.0.0.0
PORT ?= 9090

run:
	python manage.py runserver $(HOST):$(PORT)

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

m: migrate

mk: makemigrations

mm: makemigrations migrate


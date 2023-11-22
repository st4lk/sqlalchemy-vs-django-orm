DB_LOG ?=

migrate:
	alembic upgrade head

makemigrations:
	alembic revision --autogenerate -m "${COMMENT}"

unmigrate:
	alembic downgrade -1

mmigrate: makemigrations migrate

m: migrate

mm: mmigrate

mk: makemigrations

run:
	DB_LOG=$(DB_LOG) python main.py

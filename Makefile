# Makefile for fastapi-wallet-assets
.PHONY: action

# Variables
PYTHON = python
PIP = pip
PROJECT_NAME = fastapi-wallet-assets
VENV_NAME = venv

# Add new alembic migration
db-add-migration:
	alembic revision -m $(name)
db-up-all:
	alembic upgrade head
db-down-one:
	alembic downgrade -1
db-refresh-current:
	alembic downgrade -1 && alembic upgrade head

run:
	$(PYTHON) -m uvicorn app.main:fastapiApp --reload
	# fastapi dev app/main.py

run-live:
	$(PYTHON) -m uvicorn app.main:fastapiApp --workers 2
	# fastapi run app/main.py
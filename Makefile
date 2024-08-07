# Makefile for fastapi-wallet-assets
.PHONY: action

# Variables
PYTHON = python
PIP = pip
PROJECT_NAME = fastapi-wallet-assets
VENV_NAME = venv

# Add new alembic migration
add-migration:
	alembic revision -m $(name)
	


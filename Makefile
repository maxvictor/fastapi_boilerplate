install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	flake8 .

format:
	black . && isort .

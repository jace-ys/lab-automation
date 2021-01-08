DEPENDENCIES = db.redis

.PHONY: run fmt test dependencies

run:
	poetry run python -m main

fmt:
	poetry run black . --exclude vendor
	poetry run isort . --skip vendor

test:
	poetry run python -m pytest -v test

dependencies:
	docker-compose up -d ${DEPENDENCIES}

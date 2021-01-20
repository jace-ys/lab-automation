DEPENDENCIES = db.redis pubsub.redis

.PHONY: run fmt test dependencies

run:
	poetry run python -m main

fmt:
	poetry run black . --exclude vendor
	poetry run isort . --skip vendor

test:
	poetry run pytest . --ignore vendor

dependencies:
	docker-compose up -d ${DEPENDENCIES}

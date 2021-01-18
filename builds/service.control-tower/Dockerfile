FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ARG DIR="services/control-tower"

RUN apt-get update -y && \
  apt-get install -y curl

ENV POETRY_VERSION=1.1.0
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

WORKDIR /src

COPY ./vendor ./vendor
COPY ./$DIR/poetry.lock ./$DIR/pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./$DIR ./
COPY ./lib ./lib

CMD ["python", "-m", "main"]

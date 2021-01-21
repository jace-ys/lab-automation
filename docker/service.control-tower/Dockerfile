FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN apt-get update -y && \
  apt-get install -y curl

ENV POETRY_VERSION=1.1.0
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"

COPY ./vendor /vendor
COPY ./lib /lib

WORKDIR /usr/service
COPY ./services/control-tower/poetry.lock ./services/control-tower/pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./services/control-tower ./

CMD ["python", "-m", "main"]

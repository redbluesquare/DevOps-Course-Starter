FROM python:3.8.3 as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
WORKDIR /app
COPY pyproject.toml poetry.toml /app/
RUN poetry config virtualenvs.create false --local && poetry install
COPY todo_app /app/todo_app

FROM base as development
ENV FLASK_DEBUG=True
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as production
ENV FLASK_DEBUG=False
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
COPY .env.test /app/
ENTRYPOINT poetry run pytest

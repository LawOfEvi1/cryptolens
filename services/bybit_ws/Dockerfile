FROM python:3.12-slim

ENV POETRY_VERSION=2.1.3
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH=/app

CMD ["python", "main.py"]

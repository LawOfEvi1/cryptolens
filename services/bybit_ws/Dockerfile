# 1. Базовый образ с поддержкой Poetry и Python
FROM python:3.12-slim

# 2. Установим Poetry
ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

# 3. Установим рабочую директорию
WORKDIR /app

# 4. Скопируем файлы проекта
# COPY pyproject.toml poetry.lock ./
# COPY common ./common
# COPY kline_service ./kline_service
# COPY main.py ./main.py
COPY . .

# 5. Установим зависимости через Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# 6. Установим переменную окружения для импорта из `common/`
ENV PYTHONPATH=/app

# 7. Запуск скрипта
CMD ["python", "main.py"]

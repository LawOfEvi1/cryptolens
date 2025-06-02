# Используем образ с Python 3.12
FROM python:3.12-slim

# Устанавливаем Poetry
ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

# Устанавливаем netcat-openbsd (для команды `nc`)
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер (код db_api)
COPY . /app/

# Копируем конфигурационные файлы из соседней папки config в контейнер
COPY ../config /config

# Копируем и даём права на скрипт запуска
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Добавляем /config в PYTHONPATH для импорта настроек
ENV PYTHONPATH=/app:/config

# Запускаем приложение
CMD ["/entrypoint.sh"]

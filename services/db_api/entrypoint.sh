#!/bin/bash

# Ждем, пока PostgreSQL будет доступен
echo "⏳ Waiting for PostgreSQL to start..."
while ! nc -z postgres 5432; do
  sleep 0.5
done
echo "✅ PostgreSQL is up!"

# Запускаем миграции Alembic
echo "📦 Running Alembic migrations..."
poetry run alembic upgrade head

# Запускаем FastAPI-приложение
echo "🚀 Starting FastAPI app..."
exec poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000


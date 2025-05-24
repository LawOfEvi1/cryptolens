# Monorepo для микросервисного проекта на Python

## Описание проекта

Этот репозиторий содержит несколько микросервисов, реализующих комплексную систему сбора, обработки и отображения данных с использованием Kafka, Redis, FastAPI и других современных инструментов.

---

## Архитектура и структура проекта

monorepo/
├── services/
│ ├── bot/ # Telegram бот для взаимодействия и настройки через Redis
│ ├── bybit_ws/ # Подписка на WebSocket Bybit → продюсер Kafka
│ ├── consumer_service/ # Консьюмер Kafka, аналитика, запись в БД
│ ├── db_api/ # FastAPI + SQLAlchemy, API для хранения данных и настроек
│ └── chart_online/ # Сервисы для построения онлайн графиков из Kafka
│ ├── book_order_chart_online/
│ ├── trade_chart_online/
│ └── liquidation_chart_online/
│
├── libs/
│ └── common_lib/ # Общие библиотеки: модели, утилиты, темы Kafka
│
├── infra/
│ ├── docker-compose.yml # Конфигурация для запуска всех сервисов и зависимостей (Redis, Kafka, БД)
│ └── kafka-ui/ # Веб-интерфейс для Kafka (docker)
│
├── tests/ # Тесты для каждого сервиса
│
├── pyproject.toml # Управление зависимостями Poetry
├── Makefile # Утилиты для запуска, тестирования, сборки
└── README.md # Этот файл

yaml
Copy
Edit

---

## Основные технологии

- Python 3.11+
- FastAPI
- Kafka (асинхронные продюсеры и консьюмеры)
- Redis
- PostgreSQL + SQLAlchemy
- Poetry для управления зависимостями
- Docker и Docker Compose для контейнеризации и оркестрации
- Pytest для тестирования

---

## Быстрый старт

1. Клонируйте репозиторий:

```bash
git clone https://github.com/LawOfEvi1/CryptoLens.git
cd monorepo
Запустите инфраструктуру (Kafka, Redis, PostgreSQL и UI):

bash
Copy
Edit
docker-compose -f infra/docker-compose.yml up -d
Запустите нужный сервис (пример для bot):

bash
Copy
Edit
cd services/bot
poetry install
poetry run python main.py
Или через Makefile (если настроено):

bash
Copy
Edit
make run-bot
Тестирование
Запуск тестов для всех сервисов:

bash
Copy
Edit
make test
Или для конкретного сервиса:

bash
Copy
Edit
cd services/bot
poetry run pytest
Структура сервисов и их назначение
bot — Telegram бот для управления настройками (использует Redis для хранения временных данных)

bybit_ws — подписка на WebSocket Bybit и отправка сообщений в Kafka

consumer_service — обработка сообщений из Kafka, аналитика и запись в PostgreSQL

db_api — FastAPI сервис с REST API для взаимодействия с базой данных и настройками

chart_online/ — микросервисы для генерации и отображения онлайн-графиков на основе данных Kafka

Особенности разработки
Используется единый Makefile для удобства запуска, тестирования и сборки

Общие библиотеки находятся в libs/common_lib, которые используются всеми сервисами

Контейнеры и зависимости подняты через Docker Compose в папке infra

Рекомендуется использовать Poetry для управления виртуальными окружениями и зависимостями

Планы и дальнейшее развитие
Добавить клиентские приложения для iOS и Android для отображения графиков

Расширить покрытие тестами и интеграционные тесты

Улучшить CI/CD пайплайн для автоматической сборки и деплоя

Контакты и обратная связь
Если у вас есть вопросы или предложения, пишите в Issues или на email: your.email@example.com

Спасибо за интерес к проекту!

yaml
Copy
Edit

---

Если хочешь, могу помочь сделать еще более кастомный ридми под твой стиль.







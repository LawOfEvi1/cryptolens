import os

structure = {
    "services": {
        "bot": {
            "mappers": {
                "__init__.py": "",
                "extended_mapper.py": "# Расширенные мапперы"
            },
            "models": {},
            "handlers": {},
            "pyproject.toml": "[tool.poetry]\nname = \"bot\"\nversion = \"0.1.0\""
        },
        "bybit_ws": {
            "pyproject.toml": "[tool.poetry]\nname = \"bybit_ws\"\nversion = \"0.1.0\""
        }
    },
    "libs": {
        "common_lib": {
            "kafka_topics.py": "# Общие топики Kafka",
            "models.py": "# Общие модели",
            "utils.py": "# Утилиты",
            "mappers": {
                "base_mapper.py": "# Абстрактные базовые классы для мапперов",
                "some_entity_mapper.py": "# Конкретные реализации мапперов"
            },
            "pyproject.toml": "[tool.poetry]\nname = \"common_lib\"\nversion = \"0.1.0\""
        }
    },
    "infra": {
        "docker-compose.yml": "# Docker Compose config",
        "kafka-ui": {}
    },
    "tests": {
        "bot": {}
    },
    "pyproject.toml": "[tool.poetry]\nname = \"CryptoLens\"\nversion = \"0.1.0\"",
    "Makefile": "# Makefile команды",
    "README.md": "# README",
    ".gitignore": "# .gitignore"
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Структура проекта создана.")

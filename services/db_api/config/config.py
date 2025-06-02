from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


env_file = os.getenv("ENV_FILE", "settings.env.local")

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TB_TOKEN: str
    TB_CHAT_ID: str
    BB_KEY: str
    BB_SECRET: str

    # @property
    # def DATABASE_URL_asyncpg(self):

    @property
    def DATABASE_URL_asyncpg(self):
        # DSN
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=env_file)




dotenv_path = os.path.join(os.path.dirname(__file__), env_file)
load_dotenv(dotenv_path)


try:
    settings = Settings()
    print("Settings loaded successfully.")
except Exception as e:
    print("Error loading settings:", e)

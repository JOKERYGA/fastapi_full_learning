from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    MODE: str = "DEV"

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SMTP_USER: str
    SMTP_PASSWORD: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env" if os.getenv('MODE') != 'TEST' else ".test.env")


settings = Settings()


# from dotenv import load_dotenv
# import os

# load_dotenv()

# # environ - берет зависимости из словаря переменного окружения
# DB_HOST = os.environ.get("DB_HOST")
# DB_PORT = os.environ.get("DB_PORT")
# DB_NAME = os.environ.get("DB_NAME")
# DB_USER = os.environ.get("DB_USER")
# DB_PASS = os.environ.get("DB_PASS")

# DB_PORT_TEST=os.environ.get("DB_HOST_TEST")
# DB_HOST_TEST=os.environ.get("DB_PORT_TEST")
# DB_NAME_TEST=os.environ.get("DB_NAME_TEST")
# DB_USER_TEST=os.environ.get("DB_USER_TEST")
# DB_PASS_TEST=os.environ.get("DB_PASS_TEST")


# # SECRET_AUTH = os.environ.get("SECRET_AUTH")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

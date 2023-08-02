from pydantic import BaseSettings


class EnvSetting(BaseSettings):
    PORT = ""
    ENV = ""
    URL = ""

    class Config:
        env_file = "app/.env"

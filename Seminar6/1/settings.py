from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str #= 'sqlite:///mydatabase.db'

class Config:
    env_file = '.env'


settings = Settings()
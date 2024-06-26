from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DatabaseSettings(Base):
    DB_HOST: str
    DB_PORT: str | int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_syncpg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class DataSettings(Base):
    data_directory: str
    csv_storage: str


db_settings = DatabaseSettings()
data_settings = DataSettings()

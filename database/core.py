from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from configs.settings import db_settings
from database.models import Base


class DatabaseCore:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    @staticmethod
    async def drop_database() -> None:
        async with db_core.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    @staticmethod
    async def create_tables() -> None:
        async with db_core.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db_core = DatabaseCore(url=db_settings.database_url_asyncpg, echo=db_settings.db_echo)


async def restart_database():
    await db_core.drop_database()
    await db_core.create_tables()

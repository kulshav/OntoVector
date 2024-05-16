from datetime import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, BIGINT
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, declared_attr

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    # TODO: repr
    def __repr__(self):
        pass


class Document(Base):
    id: Mapped[intpk]
    name: Mapped[str]
    size: Mapped[float]
    created_at: Mapped[datetime]


class Vector(Base):
    id: Mapped[int] = mapped_column(BIGINT, ForeignKey("documents.id"))
    embedding: Mapped[list[float | int]]

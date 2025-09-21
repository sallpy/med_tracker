from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import Text


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Text)
    password: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text)


class Analysis(Base):
    __tablename__ = 'analysis'

    id: Mapped[int] = mapped_column(primary_key=True)
    type_of_analysis: Mapped[str]
    type_of_test: Mapped[str]
    due_date: Mapped[datetime]
    result: Mapped[float]

    # user: Mapped[User | None] = relationship()

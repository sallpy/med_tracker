from typing import Annotated, Any, Generator
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import settings
from model import Base

engine = create_engine(url=settings.DB_URL)

sync_session = sessionmaker(bind=engine)


def get_session() -> Generator[Session, Any, None]:
    with sync_session() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def setup_tables():
    Base.metadata.create_all(engine)

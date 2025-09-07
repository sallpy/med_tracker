from .base import Base
from sqlalchemy.orm import Mapped

class Tests(Base):
    type_of_tests: Mapped[str]
    date: Mapped[str]
    results: Mapped[float]
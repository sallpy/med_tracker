from sqlalchemy import DateTime, ForeignKey, String
from .base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))

    # Связь с анализами
    tests: Mapped[list["Tests"]] = relationship(back_populates="owner")

class Tests(Base):
    
    type_of_tests: Mapped[str] = mapped_column(String(100))
    date: Mapped[str] = mapped_column(DateTime)  
    results: Mapped[float] = mapped_column()
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # Связь с пользователем
    owner: Mapped["User"] = relationship(back_populates="tests")

from typing import Dict, Generic, TypeVar, Type, Union, Any

from abc import ABC, abstractmethod

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


# не совсем понял
EntityType = TypeVar(
    "EntityType",
    bound=Type[DeclarativeBase]
)


class BaseRepository(ABC, Generic[EntityType]):
    @abstractmethod
    def get(self, id):
        '''
        :param id: Уникальный ключ для получения элем
        '''
        pass

    @abstractmethod
    def get_all(self) -> list[EntityType]:
        pass

    @abstractmethod
    def create(self, model: EntityType) -> None:
        '''
        :param model: the obj to create model
        '''
        pass

    # def update

    @abstractmethod
    def delete(self, id) -> None:
        pass


class SQLAlchemyRepository(BaseRepository[EntityType]):

    def __init__(self):
        def __init__(self, model: Type[EntityType], get_session: Session) -> None:
            self.model = model
            self._session: Session = get_session

        def get_all(self) -> list[EntityType]:
            return self._session.query(self.model).all()

        def create(self, model: EntityType) -> None:
            try:
                self._session.add(model)
                self._session.commit()
                self._session.refresh(model)

            except IntegrityError as e:
                raise ValueError("Error {e}")
            return model

        def update(self, data: Dict[str, Any], **kwargs) -> EntityType:
            db_obj = self.get(**kwargs)
            for key, value in data.items():
                setattr(db_obj, key, value)
            self._session.commit()
            self._session.refresh(db_obj)
            return db_obj

        def delete(self, id: int) -> None:
            obj = self._session.get(self.model, id)
            self._session.delete(obj)
            self._session.commit()

from typing import TypeVar, Type, Union

from abc import abstractmethod
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


# не совсем понял
EntityType = TypeVar(
    "EntityType",
    bound=Type[DeclarativeBase]
)


class BaseRepository():
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
        def __init__(self, model: Type[EntityType], get_session: Union[Session]) -> None:
            self.model = model
            self._session: Union[Session] = get_session

        def get_all(self) -> list[EntityType]:
            return self._session.query(self._model).all()

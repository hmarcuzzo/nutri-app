from fastutils_hmarcuzzo.common.database.sqlalchemy.base_repository import BaseRepository
from sqlalchemy.orm import Session

from src.dto.create_user_dto import CreateUserDto
from src.entities.user_entity import User


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

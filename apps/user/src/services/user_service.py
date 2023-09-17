from sqlalchemy.orm import Session

from src.dto.create_user_dto import CreateUserDto
from src.dto.user_dto import UserDto
from src.entities.user_entity import User
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    # ---------------------- PUBLIC METHODS ----------------------
    async def create_user(self, user_dto: CreateUserDto, db_session: Session) -> UserDto | None:
        # user = await self.__verify_email_exist(user_dto.email, db_session)

        # if user:
        #     raise BadRequestException(f"Email already in use.", ["User", "email"])

        new_user = await self.user_repository.create(db_session, user_dto)
        new_user = self.user_repository.save(db_session, new_user)

        response = UserDto(**new_user.__dict__)
        return UserDto(**new_user.__dict__)

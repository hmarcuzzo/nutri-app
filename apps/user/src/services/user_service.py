from fastutils_hmarcuzzo.types.delete_result import DeleteResult
from fastutils_hmarcuzzo.types.exceptions import BadRequestException
from fastutils_hmarcuzzo.types.find_one_options import FindOneOptions
from fastutils_hmarcuzzo.types.update_result import UpdateResult
from sqlalchemy.orm import Session

from src.dto.create_user_dto import CreateUserDto
from src.dto.update_user_dto import UpdateUserDto
from src.dto.user_dto import UserDto
from src.entities.user_entity import User
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    # ---------------------- PUBLIC METHODS ----------------------
    async def create_user(self, user_dto: CreateUserDto, db_session: Session) -> UserDto:
        user = await self.__verify_email_exist(db_session, user_dto.email)

        if user:
            raise BadRequestException(f"Email already in use.", ["User", "email"])

        new_user = await self.user_repository.create(db_session, user_dto)
        new_user = self.user_repository.save(db_session, new_user)

        return UserDto(**new_user.__dict__)

    async def find_one_user(self, find_data: FindOneOptions | str, db_session: Session) -> UserDto:
        user = await self.user_repository.find_one_or_fail(db_session, find_data)

        return UserDto(**user.__dict__)

    async def delete_user(self, user_id: str, db_session: Session) -> DeleteResult:
        return await self.user_repository.delete(db_session, user_id)

    async def update_user(
        self, user_id: str, update_user_dto: UpdateUserDto, db_session: Session
    ) -> UpdateResult:
        if update_user_dto.email:
            user = await self.__verify_email_exist(db_session, update_user_dto.email)

            if user:
                raise BadRequestException(f"Email already in use.", ["User", "email"])

        response = await self.user_repository.update(db_session, user_id, update_user_dto)
        return response

    async def __verify_email_exist(self, db_session: Session, email: str) -> User:
        return await self.user_repository.find_one(db_session, {"where": User.email == email})

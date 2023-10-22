from math import ceil

from fastutils_hmarcuzzo.types.custom_pages import Page
from fastutils_hmarcuzzo.types.delete_result import DeleteResult
from fastutils_hmarcuzzo.types.exceptions import BadRequestException
from fastutils_hmarcuzzo.types.find_many_options import FindManyOptions
from fastutils_hmarcuzzo.types.find_one_options import FindOneOptions
from fastutils_hmarcuzzo.types.update_result import UpdateResult
from fastutils_hmarcuzzo.utils.pagination_utils import PaginationUtils
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

        return UserDto.model_validate(new_user)

    async def find_one_user(self, find_data: FindOneOptions | str, db_session: Session) -> UserDto:
        user = await self.user_repository.find_one_or_fail(db_session, find_data)

        return UserDto.model_validate(user)

    async def get_all_users(
        self, pagination: FindManyOptions, db_session: Session
    ) -> Page[UserDto]:
        [all_users, total] = await self.user_repository.find_and_count(
            db_session,
            pagination,
        )

        users_dto = []
        for user in all_users:
            users_dto.append(UserDto.model_validate(user))

        return PaginationUtils.generate_page(
            users_dto, total, pagination["skip"], pagination["take"]
        )

    async def delete_user(self, user_id: str, db_session: Session) -> DeleteResult:
        return await self.user_repository.delete(db_session, user_id)

    async def update_user(
        self, user_id: str, update_user_dto: UpdateUserDto, db_session: Session
    ) -> UpdateResult:
        if update_user_dto.email:
            user = await self.__verify_email_exist(db_session, update_user_dto.email)

            if user:
                raise BadRequestException(f"Email already in use.", ["User", "email"])

        return await self.user_repository.update(db_session, user_id, update_user_dto)

    async def __verify_email_exist(self, db_session: Session, email: str) -> User:
        return await self.user_repository.find_one(db_session, {"where": User.email == email})

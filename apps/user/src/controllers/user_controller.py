from uuid import UUID

from fastapi import APIRouter, Depends
from fastutils_hmarcuzzo.decorators.pagination_decorator import PaginationOptionsProvider
from fastutils_hmarcuzzo.types.custom_pages import Page
from fastutils_hmarcuzzo.types.delete_result import DeleteResult
from fastutils_hmarcuzzo.types.update_result import UpdateResult
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.status import HTTP_201_CREATED

from src.database.db_connection import get_user_db
from src.dto.create_user_dto import CreateUserDto
from src.dto.update_user_dto import UpdateUserDto
from src.dto.user_dto import UserDto
from src.services.user_service import UserService

user_router = APIRouter(tags=["Users"], prefix="/user")

user_service = UserService()


@user_router.post(
    "/create",
    status_code=HTTP_201_CREATED,
    response_model=UserDto,
)
async def create_user(request: CreateUserDto, database: Session = Depends(get_user_db)) -> UserDto:
    return await user_service.create_user(request, database)


@user_router.get(
    "/get",
    response_model=Page[UserDto],
    response_model_exclude_unset=True,
)
async def get_all_users(
    pagination=Depends(PaginationOptionsProvider()),
    database: Session = Depends(get_user_db),
) -> Page[UserDto]:
    return await user_service.get_all_users(pagination, database)


#
@user_router.get("/get/{id}", response_model=UserDto)
async def get_user_by_id(id: UUID, database: Session = Depends(get_user_db)) -> UserDto:
    return await user_service.find_one_user(str(id), database)


# @user_router.delete("/delete", response_model=DeleteResult)
# async def delete_user(
#     user=Depends(get_current_user), database: Session = Depends(get_user_db)
# ) -> DeleteResult:
#     return await user_service.delete_user(str(user.id), database)
#
#
# @user_router.patch("/update", response_model=UpdateResult)
# async def update_user(
#     request: UpdateUserDto,
#     user=Depends(get_current_user),
#     database: Session = Depends(get_user_db),
# ) -> UpdateResult:
#     return await user_service.update_user(str(user.id), request, database)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from src.database.db_connection import get_user_db
from src.dto.create_user_dto import CreateUserDto
from src.dto.user_dto import UserDto
from src.services.user_service import UserService

user_router = APIRouter(tags=["Users"], prefix="/user")

user_service = UserService()


@user_router.post(
    "/create",
    status_code=HTTP_201_CREATED,
    response_model=UserDto,
)
async def create_user(
    request: CreateUserDto, database: Session = Depends(get_user_db)
) -> UserDto | None:
    return await user_service.create_user(request, database)


# @user_router.get(
#     "/get",
#     response_model=PaginationResponseDto[UserDto],
#     response_model_exclude_unset=True,
#     dependencies=[Depends(Auth([UserRole.ADMIN]))],
# )
# async def get_all_users(
#     pagination: FindManyOptions = Depends(
#         GetPagination(User, UserDto, FindAllUserQueryDto, OrderByUserQueryDto)
#     ),
#     database: Session = Depends(get_db),
# ) -> Optional[PaginationResponseDto[UserDto]]:
#     return await user_service.get_all_users(pagination, database)
#
#
# @user_router.get(
#     "/get/{id}", response_model=UserDto, dependencies=[Depends(Auth([UserRole.ADMIN]))]
# )
# async def get_user_by_id(id: UUID, database: Session = Depends(get_db)) -> Optional[UserDto]:
#     return await user_service.find_one_user(str(id), database)
#
#
# @user_router.delete("/delete", response_model=UpdateResult, dependencies=[Depends(Auth())])
# async def delete_user(
#     user: User = Depends(get_current_user), database: Session = Depends(get_db)
# ) -> Optional[UpdateResult]:
#     return await user_service.delete_user(str(id), database)
#
#
# @user_router.patch("/update", response_model=UpdateResult, dependencies=[Depends(Auth())])
# async def update_user(
#     request: UpdateUserDto,
#     user: User = Depends(get_current_user),
#     database: Session = Depends(get_db),
# ) -> Optional[UpdateResult]:
#     return await user_service.update_user(str(id), request, database)

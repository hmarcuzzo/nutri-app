from datetime import datetime

from constants.Enum.user_role import UserRole
from fastutils_hmarcuzzo.common.dto.base_dto import BaseDto


class UserDto(BaseDto):
    email: str
    role: UserRole
    last_access: datetime | None

    class Config:
        from_attributes = True

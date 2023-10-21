from datetime import datetime

from fastutils_hmarcuzzo.common.dto.base_dto import BaseDto
from nutri_app_core.constants.Enum.user_role import UserRole


class UserDto(BaseDto):
    email: str
    role: UserRole
    last_access: datetime | None

    class Config:
        from_attributes = True

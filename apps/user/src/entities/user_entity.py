from dataclasses import dataclass

from fastutils_hmarcuzzo.common.database.sqlalchemy.base_entity import BaseEntity
from fastutils_hmarcuzzo.utils.hash import generate_hash
from nutri_app_core.constants.Enum.user_role import UserRole
from sqlalchemy import Column, DateTime, Enum, String, event
from sqlalchemy_utils import EmailType, PasswordType, has_changes


@dataclass
class User(BaseEntity):
    email = Column(EmailType(255), nullable=False, unique=True)
    password = Column(PasswordType(schemes=["argon2"]), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)
    last_access = Column(DateTime, nullable=True)

    def __init__(
        self,
        email: EmailType,
        password: PasswordType,
        role: UserRole = UserRole.USER,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.role = role


# @event.listens_for(User, "before_insert")
# @event.listens_for(User, "before_update")
# def before_insert(mapper, connection, target: User) -> None:
#     if has_changes(target, "password"):
#         target.password = generate_hash(target.password)

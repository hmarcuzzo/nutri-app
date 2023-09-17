from sqlalchemy.orm import Session

from src.dto.create_user_dto import CreateUserDto
from src.entities.user_entity import User


class UserRepository:
    async def create(self, db_session: Session, user_dto: CreateUserDto) -> User:
        new_user = User(**user_dto.model_dump(exclude_unset=True))

        db_session.add(new_user)
        db_session.flush()

        return new_user

    def save(self, db_session: Session, user: User | None) -> User | None:
        db_session.commit()

        if user:
            db_session.refresh(user)

        return user

    def get_by_id(self, user_id: int, db_session: Session) -> User | None:
        return db_session.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str, db_session: Session) -> User | None:
        return db_session.query(User).filter(User.email == email).first()

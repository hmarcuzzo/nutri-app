from fastutils_hmarcuzzo.common.database.sqlalchemy import DatabaseSessionManager
from sqlalchemy.orm import Session

from config.config import (
    DATABASE_CONNECTION,
    DATABASE_USERNAME,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    APP_TZ,
)


def get_database_url() -> str:
    return f"{DATABASE_CONNECTION}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


db_session = DatabaseSessionManager(get_database_url(), APP_TZ)


def get_user_db() -> Session:
    db = db_session.get_db()
    try:
        yield next(db)
    finally:
        db.close()

from fastapi import APIRouter

from src.controllers.user_controller import user_router
from src.entities.user_entity import User

user_routers = APIRouter()

user_routers.include_router(user_router)

user_entities = [User]

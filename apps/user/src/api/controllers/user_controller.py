from django.urls import path
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.user.src.api.dto.create_user_dto import CreateUserDto


@swagger_auto_schema(
    method='post',
    tags=['User'],
    operation_description='Create a new user',
    operation_id='Create User',
    request_body=CreateUserDto,
)
@api_view(['POST'])
def create_user(request: CreateUserDto):
    return Response(status=status.HTTP_201_CREATED)


urlpatterns  = [
    path('create/', create_user, name='create-user'),
]



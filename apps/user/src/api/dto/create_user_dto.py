from rest_framework import serializers


class CreateUserDto(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.db import models
from django.forms import EmailField, CharField, DateTimeField


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email: EmailField = models.EmailField(max_length=120, unique=True)
    password: CharField = models.CharField(max_length=120)
    role: CharField = models.CharField(
        max_length=20,
        choices=[('admin', 'admin'), ('user', 'user')],
        default='user'
    )
    last_access: DateTimeField = models.DateTimeField(null=True)

    def check_password(self, raw_password) -> bool:
        return check_password(raw_password, self.password)

    class Meta:
        db_table = 'user'
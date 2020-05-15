from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,User

#扩展用户模型
class MyUser(AbstractUser):
    user_type=models.IntegerField(default=2)
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='电话')
    avatar = models.ImageField(verbose_name='用户头像', upload_to='avatar/%Y/')

# class User(models.Model):
#     username=models.CharField(max_length=20,verbose_name='用户名')
#     password=models.CharField(max_length=20,verbose_name='密码')
#
#     pass
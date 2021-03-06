from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """用户模型类"""
    # 增加 mobile 字段
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        # 表名
        db_table = 'tb_users'
        verbose_name = '用户'

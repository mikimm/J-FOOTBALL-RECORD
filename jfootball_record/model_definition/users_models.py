from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

class Gender(models.IntegerChoices):
        MAN = 1
        WOMAN = 2
        
class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    gender = models.IntegerField(choices=Gender)
    groups = models.ManyToManyField(
            Group,
            verbose_name=('groups'),
            blank=True,
            help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
            related_name="jfootball_record_user_groups",
            related_query_name="user",
        ),
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="jfootball_record_user_permissions",
        related_query_name="user",
    )


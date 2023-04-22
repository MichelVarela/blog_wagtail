from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
# Create your models here.


class UserManager(BaseUserManager):


    def create_user(
        self,
        email,
        password,
    ):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.save()
        return user


    def create_superuser(
        self,
        email,
        password,
    ):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.is_active = 1
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    activated = models.IntegerField(default=True)
    created = models.DateTimeField(blank=True, null=True, default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    objects = UserManager()


    class Meta:
        db_table = 'users'


    def __str__(self):
        return self.email
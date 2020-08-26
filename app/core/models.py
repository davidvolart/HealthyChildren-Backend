from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique= True)
    name = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(0.00))
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal(0.00))
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
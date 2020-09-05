from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('email is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super_user"""
        super_user = self.create_user(email=email, password=password)
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()
        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique= True)
    name = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(0.00))
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal(0.00))
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
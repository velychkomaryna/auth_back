from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(**kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Position(models.Model):

    class Role(models.TextChoices):
        PM = 'project manager'
        DEV = 'developer'
        QA = "qa engineer"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(choices=Role.choices, max_length=24)


class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.OneToOneField(Position, on_delete=models.CASCADE)
    date_of_employment = models.DateField(verbose_name=("The date of emoloyment"), auto_now_add=True)
    is_active = models.BooleanField(default=True)

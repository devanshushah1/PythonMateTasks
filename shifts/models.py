from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class ClientManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Please Enter an Email')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be None.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = ClientManager()

    def __str__(self):
        return self.email


class Shift(models.Model):
    repeat_options = [
        ('None', 'None'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
    ]
    shift_options = [
        ("Morning Shift - 5am to 9am", "Morning Shift - 5am to 9am")
    ]
    created_by = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    repeat = models.CharField(max_length=50, choices=repeat_options)
    shift_availibility = models.CharField(max_length=100, choices=shift_options)
    weekdays = models.CharField(max_length=50)

    def get_weekdays(self):
        days = self.weekdays.split(', ')
        return days

    



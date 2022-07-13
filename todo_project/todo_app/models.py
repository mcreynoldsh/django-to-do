from django.db import models
from django.contrib.auth.models import (AbstractUser)

# Inheriting from 'AbstractUser' lets us use all the fields of the default User,
# and overwrite the fields we need to change
# This is different from 'AbstractBaseUser', which only gets the password management features from the default User,
# and needs the developer to define other relevant fields.
class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self) -> str:
        return self.email

class ToDo(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    user= models.ForeignKey(AppUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
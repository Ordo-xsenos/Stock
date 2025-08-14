from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='images/', height_field='height', width_field='width')
    height = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        self.email = self.user.email
        self.username = self.user.username

        super().save(*args, **kwargs)

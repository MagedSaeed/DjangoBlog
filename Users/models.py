from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        saved_image = Image.open(self.img.path)
        if saved_image.height > 300 or saved_image.width > 300:
            saved_image.thumbnail((300, 300))
            saved_image.save(self.image.path)

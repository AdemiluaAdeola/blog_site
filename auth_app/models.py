from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='download.png', upload_to='profile/')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
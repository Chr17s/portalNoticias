from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # AbstractUser ya incluye username, email, first_name y last_name.
    avatar = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username
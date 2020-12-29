from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Upload(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_upload = models.FileField(upload_to='users')

    def __str__(self):
        return self.uploader

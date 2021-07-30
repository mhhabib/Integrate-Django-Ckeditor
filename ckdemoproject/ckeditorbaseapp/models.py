import django
from django import contrib
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class CreateCkPost(models.Model):
    title=models.CharField(max_length=300)
    description=RichTextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.title[:100]}...'

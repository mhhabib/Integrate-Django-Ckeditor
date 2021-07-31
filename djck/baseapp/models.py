from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class CreatePost(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title[:100]}..'

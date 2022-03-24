from django.db import models
from django.contrib.auth.models import User
# from froala_editor.fields import FroalaEditor
# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
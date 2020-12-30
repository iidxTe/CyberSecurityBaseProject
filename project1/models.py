import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Blog(models.Model):
    blog_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_header = models.CharField(max_length=100, default='Header')
    blog_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_header

    def __str__(self):
        return self.blog_text	

    def __str__(self):
        return self.blog_owner
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User 


class Blog(models.Model):
    title = models.CharField(max_length=30)
    desc = RichTextField()
    slug = models.CharField(max_length=30,unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogComments(models.Model):
    comment=models.ForeignKey(Blog,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.comment} by {self.author}'
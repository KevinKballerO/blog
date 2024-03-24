from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, 
                               on_delete = models.CASCADE,
                               related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,
                              on_delete = models.CASCADE)
    author = models.ForeignKey(User,
                               on_delete = models.CASCADE)
    content = models.TextField()   
    
    def __str__(self):
        return self.post.title

class Meta:
    ordering = {'-publish'}








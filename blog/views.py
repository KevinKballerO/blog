from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .models import Comment
from .serializer import PostSerializer
from .serializer import CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


        


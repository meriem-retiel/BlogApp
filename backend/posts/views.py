from django.contrib.auth import get_user_model
from django.shortcuts import render
from .models import Post 
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer



class UserViewset(viewsets.ModelViewSet):
    queryset= get_user_model().objects.all()
    serializer_class = UserSerializer


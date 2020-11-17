from myblog.models import Blog, Article
from rest_framework import viewsets, permissions 
from .serializers import BlogSerializer,ArticleSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    permission_classes={
        permissions.AllowAny
    }
    serializer_class=BlogSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    permission_classes={
        permissions.AllowAny
    }
    serializer_class=ArticleSerializer
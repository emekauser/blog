from rest_framework import serializers
from myblog.models import Blog, Article

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields="__all__"
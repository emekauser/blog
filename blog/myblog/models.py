from django.db import models

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=100)
    des=models.CharField(max_length=500, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title=models.CharField(max_length=500)
    body=models.CharField(max_length=2000, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    

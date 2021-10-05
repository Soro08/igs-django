from django.shortcuts import render
from rest_framework import viewsets

from blog.serializers import CategorySerializer, ArticleSerializer
from blog.models import Category, Article

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

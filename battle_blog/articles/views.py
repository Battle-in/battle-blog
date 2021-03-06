from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('update_time')
    serializer_class = ArticleSerializer

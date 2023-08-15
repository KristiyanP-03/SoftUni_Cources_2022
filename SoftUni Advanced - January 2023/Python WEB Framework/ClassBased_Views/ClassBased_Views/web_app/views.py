from django.shortcuts import render
from django.views.generic import ListView
from ClassBased_Views.web_app.models import Article


# Create your views here.
class ArticleView(ListView):
    template_name = "article.html"
    model = Article
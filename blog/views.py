from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
    ListView,
)

from .models import Article

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()#blog/modelname_list.html


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()
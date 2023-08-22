from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    ListView,
)

from .models import Article

class ArticleListView(FormView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()#blog/modelname_list.html



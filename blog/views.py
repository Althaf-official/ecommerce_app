from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
    ListView,
)


from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    queryset = Article.objects.all()


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()#blog/modelname_list.html


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()
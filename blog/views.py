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
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()#blog/modelname_list.html


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()
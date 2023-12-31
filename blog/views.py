from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = "articles/article_create.html"
    form_class=ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article,id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"

    def get_object(self):#This method is defined to retrieve the object (an article) that the view will perform deletion on.
        id_ = self.kwargs.get("id")#*extracts the value of the "id" parameter from the URL's keyword arguments
        return get_object_or_404(Article, id=id_)#! function to fetch an Article object with the specified ID from the database  #!no such object exists, it raises a 404 HTTP error

    def get_success_url(self):
        return reverse("articles:article-list")#!reverse function to generate a URL based on the URL name 
        #!articles:article-list." URL pattern defined in your Django project's URL configuration
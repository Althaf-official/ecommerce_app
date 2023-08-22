from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    )


app_name = "articles"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    path("create/", ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/", ArticleDetailView.as_view(),name="article-detail"),
]
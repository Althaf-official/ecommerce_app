from django.urls import path

from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    MyListView,
    CourseCreateView,
    )



app_name = "courses"

urlpatterns = [
    path("",MyListView.as_view(), name="courses-list"),
    #path("", my_fbv, name="courses-list"),
    path("create/",CourseCreateView.as_view(),name="course-create"),
    #path("", CourseListView.as_view(), name="courses-list"),
    #path("", CourseView.as_view(template_name="contact.html"), name="courses-list"),
    #path("<int:id>", CourseView.as_view(), name="courses-detail"),
]
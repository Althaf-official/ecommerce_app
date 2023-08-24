from django.urls import path

from .views import (
    my_fbv,
    CourseView
    )



app_name = "courses"

urlpatterns = [
    #path("", my_fbv, name="courses-list"),
    path("", CourseView.as_view(template_name="contact.html"), name="courses-list"),
    path("<int:id>", CourseView.as_view(), name="courses-detail"),
]
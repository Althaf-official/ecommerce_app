from django.shortcuts import render
from django.views import View


class CourseView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"about.html",{})


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, "about.html",{})
    # this is function base view example
from django.shortcuts import render,get_object_or_404
from django.views import View
#BASE CLASS VIEW =View

from .models import Course
from .forms import CourseModelForm

class CourseUpdateView(View):
    template_name = "courses/course_update.html"
    def get_object(self)


    def get(self,request, *args,**kwargs):
        #GET Method
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self,request, *args,**kwargs):
        #POST Method
        form = CourseModelForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = "courses/course_create.html"
    def get(self,request, *args,**kwargs):
        #GET Method
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self,request, *args,**kwargs):
        #POST Method
        form = CourseModelForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()#!This queryset will be used later to fetch data to display in the template

    def get_queryset(self):
        return self.queryset


    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name,{'object_list':self.queryset})
        #!eturn render(request, self.template_name, {'object_list': self.queryset}): This line returns an HTTP response using the render function. Here's what each part of this line does:
class MyListView(CourseListView):
    queryset = Course.objects.filter(id=1)

class CourseView(View):
    template_name = "courses/course_detail.html"
    def get(self,request, id=None ,*args,**kwargs):
        context = {}

        if id is None:
            obj = get_object_or_404(Course, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, "about.html",{})
    # this is function base view example
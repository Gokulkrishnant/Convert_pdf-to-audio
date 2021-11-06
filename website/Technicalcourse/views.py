from django.shortcuts import render
from django.http import HttpResponse

class Allcourse:
    print("hello")



def Courses(request):
    ac=Allcourse.object.all()

    return HttpResponse("<h1> This is my home page</h1>")
# Create your views here.
def detail(request,course_id):
    return HttpResponse("<h2>Course details are here</h2>")

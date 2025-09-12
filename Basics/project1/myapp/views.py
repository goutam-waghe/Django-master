from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hellow</h1>")
def student(request):
    name = "goutam"
    return render(request , 'myapp/index.html' , {'name':name})


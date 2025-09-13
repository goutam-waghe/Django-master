from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hellow</h1>")
    return render(request ,'myapp/home.html')

def about(request):
    return render(request ,'myapp/about.html')

def service(request):
    return render(request ,'myapp/service.html')

def contact(request):
    return render(request ,'myapp/contact.html')


def student(request):
    name = "goutam"
    return render(request , 'myapp/index.html' , {'name':name})


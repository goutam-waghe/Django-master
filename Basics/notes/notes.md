# Topics 
- Setup
python3 -m venv venv 
django-admin startproject project1
python manage.py startapp myapp

# myapp 
- urls.py 


# Application definition
install app in project > settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]

# myapp 
create urls.py in myapp 

# use include function to add urls
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/' , include('myapp.urls'))
]


# create view
it give the reposince on webpage and render a template 
from django.shortcuts import render 
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hellow</h1>")

# urls mapping
myapp > urls.py
from django.urls import path 
from myapp import views

urlpatterns = [
    path('' , views.home , name="home")
]


# commands

python manage.py runserver

if your start your app for first time then run this command 
python manage.py migrate 
reason : because django have build in admin pannel and admin models and we have to migrate


# create admin user 
python manage.py createsuperuser


# template 
create template directory inside yout myapp 
then create index.html yout templates directory 
myapp > templates > index.html


# views
from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def student(request):
    name = "goutam"
    return render(request , 'myapp/index.html' , {'name':name})

# the render function 
render(request, template_name, context=None, content_type=None, status=None, using=None)

request → current HTTP request object (zaroori hota hai).
template_name → kaunse HTML file render karni hai.
context (optional) → dictionary jisme tum apna data bhejte ho template ke andar.
content_type, status, using → rarely use hote hain (advanced cases).



# static Files and template 
create a folder static > myapp > style.css
Inside APP
Django khud detect kr lega No need to any kind of conig
Project Level:
STATIC_URL = '/static/' # below this add the following line
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# template 
inside main
no need to do anything 

project > setting
    template {
           'DIRS': ['templates],
    }


# tailwind in django 

# bootstrap in django


# url in django template 
template url should be this type 
 <!-- <ul>
            <li><a href="{% url "home" %}">Home</a></li>
            <li><a href="{% url "about"%}">about</a></li>
 </ul> -->

urlpatterns = [
    path('' , views.home , name="home"),
    path('about/' , views.about , name="about"),
    path('service/' , views.service , name="service"),
    path('contact/' , views.contact , name="contact"),
    path("student/", views.student, name="student")
]

name should be same in both "name" in view in {% url "about"%}

# template 

imp points
- load static {% load static %} in top html file to laod static file
- link css file to Html
<!-- - <link rel="stylesheet" href="{% static "base.css" %}"> -->
- {% extends "myapp/base.html" %} extent html template in other templates 
# include 
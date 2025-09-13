This guide will help you quickly set up a Django project with a simple app, static files, templates, and views. It also covers basics like URL routing, admin panel, templates, and more.

🔧 Setup
# Create virtual environment
python3 -m venv venv 

# Activate the virtual environment (for Linux/Mac)
source venv/bin/activate

# For Windows
venv\Scripts\activate

# Start Django Project
django-admin startproject project1

# Navigate into the project directory
cd project1

# Start an app
python manage.py startapp myapp

⚙️ Application Configuration
1. Register the App

Go to: project1/settings.py

Add 'myapp' to INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # ← Add this line
]

🌐 URL Configuration
1. Create urls.py inside myapp/

File: myapp/urls.py

from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
]

2. Update Main Project URLs

File: project1/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # ← Include app URLs
]

👀 Views
Basic View
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hellow</h1>")

Render Template View
from django.shortcuts import render

def student(request):
    name = "goutam"
    return render(request, 'myapp/index.html', {'name': name})

Render Function Overview
render(request, template_name, context=None, content_type=None, status=None, using=None)


request → current HTTP request object (required)

template_name → which HTML file to render

context (optional) → dictionary to pass data to the template

content_type, status, using → advanced use cases

🚀 Running the Server
# Run the development server
python manage.py runserver

🧱 Migrations

If you're running the project for the first time:

python manage.py migrate


Django has built-in admin models which require migration.

👮‍♂️ Create Admin User
python manage.py createsuperuser


Follow the prompts to set username, email, and password.

📝 Templates
Template Directory Setup

Create the following structure:

myapp/
├── templates/
│   └── myapp/
│       └── index.html


Then render this template using render() in views.

🎨 Static Files
Structure
myapp/
└── static/
    └── myapp/
        └── style.css

No configuration needed inside the app!
Project-level Settings (settings.py):
STATIC_URL = '/static/'

# Add this to load project-level static files (optional)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

🧩 Templates & Base HTML
Setting Templates DIR (project-level)
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],  # Add this line
        ...
    },
]

🌐 URL Routing in Templates

To create dynamic navigation in templates:

<ul>
    <li><a href="{% url 'home' %}">Home</a></li>
    <li><a href="{% url 'about' %}">About</a></li>
</ul>


Make sure URLs are defined with the same name in urls.py:

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('contact/', views.contact, name="contact"),
    path("student/", views.student, name="student"),
]

🧠 Template Tags
Load Static Files in Template

At the top of your HTML file:

{% load static %}

Link Static CSS
<link rel="stylesheet" href="{% static 'myapp/style.css' %}">

📦 Template Inheritance

Use template inheritance to reuse base layout:

{% extends "myapp/base.html" %}

📚 Extras (Future Setup)

Tailwind in Django – (To be added)

Bootstrap in Django – (To be added)

✅ Summary

This guide covers:

Django project setup

App creation

Views & URL routing

Templates

Static files

Admin panel setup

Template inheritance

Template URLs

Use this README as a quick reference for your Django projects.

from django.urls import path 
from myapp import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('about/' , views.about , name="about"),
    path('service/' , views.service , name="service"),
    path('contact/' , views.contact , name="contact"),
    path("student/", views.student, name="student")
]
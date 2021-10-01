from django.contrib import admin
from django.urls import path, include
from .views import *
import django_adminlte

urlpatterns = [
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
]
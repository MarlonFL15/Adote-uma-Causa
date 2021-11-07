from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import *


urlpatterns = [
    url('home', home, name='home'),
    url('about', about, name='about'),
    url(r'^projects/$', projects, name='projects'),
    url(r'^details/(?P<id>\d+)/$', details, name='details'),

]
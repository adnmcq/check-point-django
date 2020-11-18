from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

path('', views.index, name='index'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact'),
]
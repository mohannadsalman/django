from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns =[
    path('',views.index),
    path('welcome',views.welcome),
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
]

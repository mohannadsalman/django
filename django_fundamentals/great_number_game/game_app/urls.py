from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^word$', views.word),
    url(r'^reset$', views.clear),
]
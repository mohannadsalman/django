from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('handle_data', views.show),
]
from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('show',views.show),
    path('addshow',views.addshow),
    path('showtv/<int:id>',views.showtv),
    path('showtv/<int:id>/edit',views.showedit),
    path('showtv/<int:id>/donedit',views.edit),
    path('showtv/<int:id>/destroy',views.destroy)
]
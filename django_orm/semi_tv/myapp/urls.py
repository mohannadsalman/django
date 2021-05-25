from django.urls import path,include
from . import views
urlpatterns = [
    path('shows', views.index),
    path('addshow',views.addshow),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('edit/applyedit',views.applyedit),
    path('show/<int:id>',views.show)

]
from django.urls import path
from . import views

urlpatterns = [
    path('xx/', views.index, name='index'),
    path('', views.indexx, name='indexx'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPD/', views.addPD, name='addPD'),
    path('deletePD/<int:id>/', views.deletePD, name='deletePD'),
    path('updatePD/<int:id>/', views.updatePD, name='updatePD'),
]
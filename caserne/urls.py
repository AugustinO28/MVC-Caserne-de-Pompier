from django.urls import path
from . import views


urlpatterns = [
    path('', views.character_equipement, name='character_equipement'),
    path('character/<str:name>/', views.character_detail, name='character_detail'),
]
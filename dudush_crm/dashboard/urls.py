from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ranger/', views.ranger, name='ranger'),
]
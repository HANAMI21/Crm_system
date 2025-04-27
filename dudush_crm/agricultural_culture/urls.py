from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('cultures/',
         views.agricultural_culture_list, name='agricultural_culture_list'),
    path('cultures/delete/<int:culture_id>/',
         views.delete_culture, name='delete_culture'),
    path('cultures/edit/<int:culture_id>/', views.culture_edit, name='culture_edit'),

]

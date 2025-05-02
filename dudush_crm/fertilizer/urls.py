from django.urls import path
from . import views

urlpatterns = [
    path('fertilizers/', views.fertilizer_list, name='fertilizer_list'),
    path('fertilizers/delete/<int:fertilizer_id>/', views.delete_fertilizer, name='delete_fertilizer'),
    path('fertilizer/edit/<int:fertilizer_id>/', views.fertilizer_edit, name='fertilizer_edit'),
    path('fertilizer/add/', views.fertilizer_add, name='fertilizer_add'),
    path('fertilizers/export/', views.export_fertilizers, name='export_fertilizers'),
]

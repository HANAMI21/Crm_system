from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('supplier/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
    path('supplier/edit/<int:supplier_id>/', views.supplier_edit, name='supplier_edit'),
    path('supplier/add/', views.supplier_add, name='supplier_add'),
    path('supplier/export/', views.export_suppliers, name='export_suppliers'),

]

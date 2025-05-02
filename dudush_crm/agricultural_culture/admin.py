from django.contrib import admin
from .models import AgriculturalCulture


@admin.register(AgriculturalCulture)
class AgriculturalCultureAdmin(admin.ModelAdmin):
    list_display = ['title', 'ripening_time', 'planted_area', 'planting_date', 'field_number']
    list_filter = ['ripening_time', 'planted_area', 'planting_date', 'field_number']
    search_fields = ['title', 'ripening_time', 'planted_area']
    ordering = ['planting_date', 'field_number']
    date_hierarchy = 'planting_date'

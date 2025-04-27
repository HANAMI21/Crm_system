from .models import AgriculturalCulture
from django import forms


class AgriculturalCultureForm(forms.ModelForm):
    class Meta:
        model = AgriculturalCulture
        fields = '__all__'

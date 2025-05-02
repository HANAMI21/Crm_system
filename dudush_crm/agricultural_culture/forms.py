from .models import AgriculturalCulture
from django import forms


class AgriculturalCultureForm(forms.ModelForm):
    class Meta:
        model = AgriculturalCulture
        exclude = ['user']

from django import forms
from .models import Fertilizer


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        exclude = ['user']

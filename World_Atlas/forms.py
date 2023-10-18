from django import forms
from .models import Nation

class AtlasForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ['nation']
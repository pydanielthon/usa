from django import forms 
from .models import Formularz

class NewForm(forms.ModelForm):
    class Meta:
        model = Formularz
        fields = ['document1', 'document2', 'document3', 'link1', 'link2', 'link3']
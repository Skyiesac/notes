from django import forms
from .models import Notes

class Newnotes(forms.ModelForm):
    class Meta:
        model= Notes
        fields = ('title', 'text')
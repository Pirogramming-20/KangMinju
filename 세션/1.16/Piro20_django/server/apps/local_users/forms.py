from django import forms
from .models import LocalUser

class LocalForm(forms.ModelForm):
    class Meta():
        model = LocalUser
        fields = ('__all__')